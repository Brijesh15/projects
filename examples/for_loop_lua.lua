local items = {"apple","mango","banana"}
output=""
--local i=1
local item1 ={}
for i, item in ipairs(items) do

--   	item1[i] = item
--    	print(item[i])
--	item1 = item
--        print("i:",i)
        if i==1 then
	output = output..string.format("Fruit;%s ",item)
        else
	output = output..string.format("Fruits_%s;%s ",i,item)
        end
        print(output)
end 


local ab = "djhs:ahs"
ab = ab:gsub(":","")
print(ab)
