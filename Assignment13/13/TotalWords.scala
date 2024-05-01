object WordCount {
    def main(args: Array[String]): Unit = {
        val inputString = "This is a sample input string to count the number of words."
        val wordCount = countWords(inputString)
        println(s"Word count: $wordCount")
    }

    // def countWords(input: String): Int = {
    //     val words = input.split("\\s+")
    //     words.length
    // }

    def countWords(input: String): Int = {
        var wordCount = 0
        var inWord = false

        for (char <- input) {
            if (char.isLetter) {
                if (!inWord) {
                    wordCount += 1
                    inWord = true
                }
            } else {
                inWord = false
            }
        }
        wordCount   
  }
}
