object  WordCount{
    def main(args: Array[String]): Unit = {
        val inputString = "Sachin was the GOAT of previous generation. " +
                        "Virat is the GOAT of this generation." +
                        "No one will be the GOAT of next generation. "

        val words = inputString.split("\\s+")
        val wordCounts = words.groupBy(identity).mapValues(_.length)

        wordCounts.foreach { 
            case (word, count) => {
                println(s"$word: $count")
            }
        }     
    }
}