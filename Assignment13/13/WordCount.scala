import scala.collection.mutable

// object WordCount {
//   def main(args: Array[String]): Unit = {
//     val inputString = "This is a sample input string to count the number of words in a string."
//     val wordCounts = countWords(inputString)
//     println("Word counts:")
//     wordCounts.foreach { case (word, count) =>
//       println(s"$word: $count")
//     }
//   }

//   def countWords(input: String): mutable.Map[String, Int] = {
//     val wordCounts = mutable.Map[String, Int]()
//     var wordStart = -1
//     var word: String = ""

//     for ((char, index) <- input.zipWithIndex) {

//       if (char.isLetter) {
//         if (wordStart == -1) {
//           wordStart = index
//         }
//       } else {
//         if (wordStart != -1) {
//           word = input.substring(wordStart, index).toLowerCase
//           wordCounts(word) = wordCounts.getOrElse(word, 0) + 1
//           wordStart = -1
//         }
//       }
//     }


//     if (wordStart != -1) {
//       word = input.substring(wordStart).toLowerCase
//       wordCounts(word) = wordCounts.getOrElse(word, 0) + 1
//     }

//     wordCounts
//   }
// }

object WordCount {
  def main(args: Array[String]): Unit = {
    val inputString = "Scala is a powerful programming language. Scala is also functional."
    
    // Split the input string into words
    val words = inputString.split("\\s+")

    // Count the occurrences of each word
    val wordCounts = words.groupBy(identity).mapValues(_.length)

    // Print the word counts
    wordCounts.foreach { case (word, count) =>
      println(s"$word: $count")
    }
  }
}