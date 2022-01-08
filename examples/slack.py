import requests

#res=requests.post("https://hooks.slack.com/services/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", data={"message":"Slack notify"})
#print(res)
res=requests.get("https://hooks.slack.com/services/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")
print(res)
