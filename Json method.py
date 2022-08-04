# jsonstring to python -List
import json

# MyJsonList="[1,2,3,4,5,7,8,9]"
# print("myjsonlist type is {}".format(type(MyJsonList)))
# print("oth index value in  myjsonlist[0]is {}".format(MyJsonList[0]))
# mylist=json.loads(MyJsonList)
# print(mylist)
#
# #python to json -List
# myl=[768687,29888,3876786,4997,58908,7767878,8797,999999]
# print("myl type is {}".format(type(myl)))
# print("myl index value [0]is {}".format(myl[0]))
# myl2=json.dumps(myl)
# print("myl type of is {}".format(type(myl2)))
# print("index value in myl2[1] is {}".format(myl2[1]))


# #json to python - tuple
# MyJsontuple="(1,2,3,4,5,7,8,9)"
# print("myjsontuple type is {}".format(type(MyJsontuple)))
# print("oth index value in  myjsontuplet[2]is {}".format(MyJsontuple[0]))
# mytuple=json.loads(MyJsontuple)
# print(mytuple)

# #python to json -tuple
# myt2=(76,29,66,46,55,79,8,99)
# print("myt2 type is {}".format(type(myt2)))
# print("myt2 index value [3]is {}".format(myt2[3]))
# print(myt2)
# myt3=json.dumps(myt2)
# print(myt3)
# print("myt3 type of is {}".format(type(myt3)))
# print("index value in myt3[5] is {}".format(myt3[5]))

#json to python -str
# myjstr="India"
# print("type myjstr is {}".format(type(myjstr)))
# print("myjstr is index value is [o] {}".format(myjstr[0]))
# print("myjstr is index value is [1] {}".format(myjstr[1]))
# mystr1=json.loads(myjstr)
# print(mystr1)
# print("type of mystr1 is {}".format(type(mystr1)))

#python to json -str
# mystr1="sasidhar"
# print("type mystr1 is {}".format(type(mystr1)))
# print("indexing is [4]  {}".format((mystr1[4])))
# myjstr=json.dumps(mystr1)
# print(myjstr)
# print("type myjstr is {}".format(type(myjstr)))
# print("indexing is [2] {}".format((myjstr[2])))
# print(myjstr)

# myjsondict='{"name":"sasi","age":28}'
# print(" myjsondict type is {}".format(type(myjsondict)))
# mydict=json.loads(myjsondict)
# print("mydict is {}".format(mydict))
# myd=json.dumps(mydict)
# print(myd)
#
# mydict1=[{"name":"sasidhar","age":23},{"keyvalue":555}]
# print("type mydict1 is {}".format(type(mydict1)))
# mydict1[1].update({"c":123})
# print(mydict1)
# mydict1[1].update({"d":2323})
# print(mydict1)
#
# myt=[{"name": "sasidhar", "age": {"today":"welcome"}}, {"keyvalue": 555, "c": 123, "d": 2323},{"place":"chittor","city":"tirupati"}]
# myt[0]["welcome"]="chittor"
# print(myt)

#
# myt=[{"name": "sasidhar", "age": {"today":"welcome"}}, {"keyvalue": 555, "c": 123, "d": 2323},{"place":"chittor","city":"tirupati"}]
# myt[1].update({"kwe":"wdijhd"})
# print(myt)
#
# mydict={"name":{"please":{"welcome":{"gowthami":23}}}}
# print(mydict["name"])
# print(mydict["name"]["please"]["welcome"]["gowthami"])

# mydict={"sasidhar":{"gowthami":{"welcome":300}}}
# print(mydict["sasidhar"])
# print(mydict["sasidhar"]["gowthami"])
# print(mydict["sasidhar"]["gowthami"]["welcome"])

# mydict={"name":"sasidhr","age":28,"mark_telugu":33,"english_marks":43}
# print(type(mydict))
# mydict["marks_math"]=75
# print(mydict)


# mydict1=[{"name":"sasidhr","age":28,"mark_telugu":33,"english_marks":43},{"city":"chittoor","town":"blr"}]
# print("mydict type is {}".format(type(mydict1)))
# mydict1[0].update({"mark_math2":45})
# print(mydict1)
# mydict1[1].update({"englis_marks":99})
# print(mydict1)
# mydict1.append({"welcome":"CTR"})
# print(mydict1)
# mydict1.extend([{"marks":"welcome"}, {"welcoe":"tirupati"}])
# print(mydict1)

# mydict2='[{"name":"sasidhr","age":28,"mark_telugu":33,"english_marks":43},{"city":"chittoor","town":"blr"}]'
# print("mydict type is {}".format(type(mydict2)))
# #json to python
# mydictj=json.loads(mydict2)
# print(mydictj)
# #python to json
# print("mydict type is {}".format(type(mydict2)))
# mydicts=json.dumps(mydictj)
# print(mydicts)
#
# mydict={"sasidhar":{"gowthami":{"welcome":300}}}
# print(mydict["sasidhar"])
# print(mydict["sasidhar"]["gowthami"])
# print(mydict["sasidhar"]["gowthami"]["welcome"])



# mydict={1:{2:{3:100}}}
# print("mydict [1] is",mydict[1])
# print("mydict is", mydict[1][2])
# print(mydict[1][2][3])
#
# tsrdict={"tsr":{"ysr":{"kcr":{"ctr":{"ktr":{"rrr":100}}}}}}
# print("tsr[tsr]is",tsrdict["tsr"])
# print("ysr[ysr] is",tsrdict["tsr"]["ysr"])
# print("kcr[kcr]is",tsrdict["tsr"]["ysr"]["kcr"])
# print("kcr[ctr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"])
# print("kcr[ktr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"]["ktr"])
# print("kcr[rrr]is",tsrdict["tsr"]["ysr"]["kcr"]["ctr"]["ktr"]["rrr"])