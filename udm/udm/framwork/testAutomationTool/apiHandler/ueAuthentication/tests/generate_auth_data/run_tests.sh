#!/bin/bash

SCRIPTPATH=$(cd "$(dirname "$0")"; pwd -P)
DEFAULT_UDM_SIM="$SCRIPTPATH"/../../../../../../start_dummy_udr.sh

#set -x
type jq &>/dev/null
if (( $? != 0 ))
then
	sudo apt-get install -y jq
fi

cleanup()
{
	echo cleanup
	#shutdown everything
	[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
	#sleep 1
	kill -s SIGKILL 0
}

trap cleanup EXIT

cd "$SCRIPTPATH"

test_dir_name="$1"
#If test_dir_name is not provided then all tests are run, else a specific test is run

for tc_dir in $(find "$SCRIPTPATH"/tests/ -maxdepth 1 -mindepth 1 -type d | sort -V)
do
		if [[ "$test_dir_name" != "" ]] 
		then
			[[ "$test_dir_name" != "$(basename "$tc_dir")" ]] && continue
		fi

		cd $tc_dir

		#Delete generated artifacts from previous run
		url=""
		rm -f post_resp.json post_resp_pretty.json.tmp put_resp.json put_resp_pretty.json.tmp post_resp_headers.txt put_resp_headers.txt

		#Inputs can either be 1) POST or 2) PUT. File containing "post" in name contain input for POST request and file containing string "put" contains input for PUT request.
		#There should be only one input file for POST and one for PUT for each test case. It is fine if there is no input file for a method.
		#First POST request is sent and its response validated aginst expected response. If it matches then PUT request is sent and its result compare with expected response.
		#Response header comparison is optional. Provide expected headers in files post_exp_hdr_res.txt or put_exp_hdr.txt.

		post_request_json_file=$(find . -maxdepth 1 -iname "*post*.json" ! -iname "*res*" | head -n 1)
		if [[ "$post_request_json_file" == "" ]]
		then
			echo "$tc_dir: NO POST request json"
		else
			#Any json file containg the string res in its name is expected result file. Result files are of 2 types: 1) post_exp_res 2) put_exp_res
			#If post file is present then its expected result post_exp_res must also be present
			post_exp_resp_json_file=$(find . -maxdepth 1 -iname "*post_exp_res*.json" | head -n 1)
			if [[ "$post_exp_resp_json_file" == "" ]]
			then
				echo "$tc_dir: POST request present but NO POST RESPONSE. Skipping this test case..."
				continue
			fi
		fi

		put_request_json_file=$(find . -maxdepth 1 -iname "*put*.json" ! -iname "*res*" | head -n 1)
		if [[ "$put_request_json_file" == "" ]]
		then
			echo "$tc_dir: NO PUT request json"
		else
			#Any json file containg the string res in its name is expected result file. Result files are of 2 types: 1) post_exp_res 2) put_exp_res
			#If put file is present then its expected result put must also be present
			put_exp_resp_json_file=$(find . -maxdepth 1 -iname "*put_exp_res*.json" | head -n 1)
			if [[ "$put_exp_resp_json_file" == "" ]]
			then
				echo "$tc_dir: PUT request present but NO PUT RESPONSE. Skipping this test case..."
				continue
			fi
		fi

		post_request_sh_file=$(find . -maxdepth 1 -iname "*post*.sh" ! -iname "*res*" | head -n 1)
		if [[ "$post_request_sh_file" != "" ]]
		then
			echo "$tc_dir: POST request SH FOUND"
		fi

		put_request_sh_file=$(find . -maxdepth 1 -iname "*put*.sh" ! -iname "*res*" | head -n 1)
		if [[ "$put_request_sh_file" != "" ]]
		then
			echo "$tc_dir: PUT request SH FOUND"
		fi

		if [[ "$put_request_json_file" == "" && "$post_request_json_file" == ""  && "$post_request_sh_file" == "" && "$put_request_sh_file" == "" ]]
		then
			echo "Ignoring $tc_dir: NO INPUT available. Skipping this test case..."
			continue
		fi

		#To send erroneous messages or simulate delayed responses you may use a custom udm simulator. 
		#Any non-json file containing udm in its name is considered a custom udm simulator to run.
		#If custom simulator is not provided then default simulator is run
		udm_sim=$(find . -maxdepth 1 -iname "*udr*" ! -iname "*.json")
		if [[ "$udm_sim" == "" ]]
		then
			udm_sim="$DEFAULT_UDM_SIM"
		fi

		#Start UDM simulator in a seperate process group
		setsid bash -c "$udm_sim >/dev/null" &
		udm_pgid=$!
		sleep 3 #Wait for udm sim to start

		#Send POST request and verify its results
		if [[ "$post_request_sh_file" != "" ]]
		then
			$post_request_sh_file
		else
			if [[ "$post_request_json_file" != "" ]]
			then
				curl -s --show-error -D post_resp_headers.txt -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' 'http://127.0.0.1:9000/nudm-ueau/v1/imsi-311480012345674/security-information/generate-auth-data/' -d "$(cat "$post_request_json_file")" --request POST -o post_resp.json
				#Compare POST response body
				jq . post_resp.json > post_resp_pretty.json.tmp
				diff -w <(grep -v href post_resp_pretty.json.tmp) <(jq . "$post_exp_resp_json_file" | grep -v href)
				if (( $? != 0 ))
				then
					echo "$tc_dir FAILED: POST BODY FAILED..."
					[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
					#sleep 1
					continue
				fi
			fi
		fi
		if [ -f post_exp_hdr_res.txt ]
		then
			if [ ! -f post_resp_headers.txt ]
			then
				echo "Ignoring $tc_dir: POST RESPONSE NOT RECEIVED..."
				echo "$tc_dir: FAILED"
				[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
				#sleep 1
				continue
			else
				#Compare POST response headers - Only Content-type and Response code are compared
				diff -w <(head -n 1 post_resp_headers.txt) <(head -n 1 post_exp_hdr_res.txt)
				if (( $? != 0 ))
				then
					echo "$tc_dir FAILED: POST HEADER RESPONSE CODE FAILED..."
					[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
					#sleep 1
					continue
				fi

				diff -w <(grep '^Content-Type' post_resp_headers.txt) <(grep Content-Type post_exp_hdr_res.txt)
				if (( $? != 0 ))
				then
					echo "$tc_dir FAILED: POST HEADER CONTENT-TYPE FAILED..."
					[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
					#sleep 1
					continue
				fi
			fi

			url_tmp=$(grep '^Location' post_resp_headers.txt | sed 's/^Location: //' | sed 's/\r//')
			url=$(echo -e $url_tmp)
		fi

		if [[ "$put_request_sh_file" != "" ]]
		then
			$put_request_sh_file
		else
			#Send PUT request and verify its results
			if [[ "$put_request_json_file" != "" && "$url" != "" ]]
			then
				curl -s --show-error -D put_resp_headers.txt -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' "$url" -d "$(cat "$put_request_json_file")" --request PUT -o put_resp.json
				jq . put_resp.json > put_resp_pretty.json.tmp
				diff -w put_resp_pretty.json.tmp "$put_exp_resp_json_file"
				if (( $? != 0 ))
				then
					echo "Ignoring $tc_dir: PUT BODY FAILED..."
					[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
					#sleep 1
					continue
				fi
			fi
		fi
		if [ -f put_exp_hdr_res.txt ]
		then
			if [ ! -f put_resp_headers.txt ]
			then
				echo "Ignoring $tc_dir: PUT RESPONSE NOT RECEIVED..."
				echo "$tc_dir: FAILED"
				[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
				#sleep 1
				continue
			else
				#Compare PUT response headers - Only Content-type and Response code are compared
				diff -w <(head -n 1 put_resp_headers.txt) <(head -n 1 put_exp_hdr_res.txt)
				if (( $? != 0 ))
				then
					echo "Ignoring $tc_dir: PUT HEADER RESPONSE CODE FAILED..."
					[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
					#sleep 1
					continue
				fi

				diff -w <(grep '^Content-Type' put_resp_headers.txt) <(grep Content-Type put_exp_hdr_res.txt)
				if (( $? != 0 ))
				then
					echo "Ignoring $tc_dir: PUT HEADER CONTENT-TYPE FAILED..."
					[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run
					#sleep 1
					continue
				fi
			fi
		fi

		[ "$udm_pgid" != "" ] && kill -s SIGKILL -- -"$udm_pgid" #Kill pgid of the sim that was run

		echo ""
		echo "------------------------"
		echo "$tc_dir: PASSED"
		echo "------------------------"
done

