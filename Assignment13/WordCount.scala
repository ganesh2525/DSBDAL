val data = sc.textFile("input.txt")
data.collect
val splitdata = data.flatMap(line=>line.split(" "))
splitdata.collect
val d = splitdata.map(word=>(word,1))
d.collect
val a = d.reduceByKey(_*_)
a.collect 