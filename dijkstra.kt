fun main(){
    val map= mapOf("Bmsit1" to mapOf("Bmsit2" to 176,"Bmsit3" to 124),
        "Bmsit2" to mapOf("Bmsit1" to 176 ,"Bmsit7" to 70),
        "Bmsit3" to mapOf("Bmsit4" to 58),
        "Bmsit4" to mapOf("Bmsit5" to 46,"Bmsit6" to 54),
        "Bmsit5" to mapOf("Bmsit4" to 46),
        "Bmsit6" to mapOf("Bmsit7" to 176),
        "Bmsit7" to mapOf("Bmsit8" to 78,"Bmsit2" to 70),
        "Bmsit8" to mapOf("Bmsit9" to 130),
        "Bmsit9" to mapOf("Bmsit10" to 90),
        "Bmsit10" to mapOf("Bmsit7" to 74,"Bmsit8" to 117)
        )
    val notseen=map.toMutableMap()
    val s= mutableMapOf<String,Int>()
    val pre= mutableMapOf<String,String>()
    val path= mutableListOf<String>()
    val infinity=999999
    val start="Bmsit1"//start
    for(node in notseen.keys){
        s[node]=infinity
    }
    s[start]=0

    while(notseen.isEmpty()!=true){
        var mini=""
        for(node in notseen.keys){
            if(mini=="") {
                mini = node
            }
            else if (s[node]!!<s[mini]!!){
                mini=node
            }
        }
        for(c in map[mini]!!.keys){
            for (w in map[mini]!!.values) {
                if ((w + s[mini]!!) < s[c]!!) {
                    s[c] = w + s[mini]!!
                    pre[c] = mini
                }
            }
        }
    notseen.remove(mini)
    }
    var current ="Bmsit10"//goal
    while (current!=start){
        path.add(0,current)
        current=pre[current]!!
    }
    path.add(0,start)
    print(path)
}
