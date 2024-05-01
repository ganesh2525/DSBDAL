object Calculator {

  def main(args: Array[String]): Unit = {
    println("\nCalculator using Scala");

    var continue = true;

    while(continue){
      println("\nChoose an opeartion: ");
      println("1.Addition(+)");
      println("2.Subtraction(-)");
      println("3.Multiplication(*)");
      println("4.Division(/)");
      println("5.Exit");

      println("\nChoice: ");
      var choice = scala.io.StdIn.readLine().toInt;

      choice match {
        case 1 => addition()
        case 2 => subtraction()
        case 3 => multiplication()
        case 4 => division()
        case 5 => continue = false
        case _ => println("\nInvalid Choice!")
      }
    }
  }

  def addition(): Unit = {
    println("\nEnter first number: ")
    var num1 = scala.io.StdIn.readDouble();

    println("\nEnter second number: ")
    var num2 = scala.io.StdIn.readDouble();

    var result = num1 + num2;
    println(s"Result: $num1 + $num2 = $result")
  }

  def subtraction(): Unit = {
    println("\nEnter first number: ")
    var num1 = scala.io.StdIn.readDouble();

    println("\nEnter second number: ")
    var num2 = scala.io.StdIn.readDouble();

    var result = num1 - num2;
    println(s"Result: $num1 - $num2 = $result")
  }

  def multiplication(): Unit = {
    println("\nEnter first number: ")
    var num1 = scala.io.StdIn.readDouble();

    println("\nEnter second number: ")
    var num2 = scala.io.StdIn.readDouble();

    var result = num1 * num2;
    println(s"Result: $num1 * $num2 = $result")
  }

  def division(): Unit = {
    println("\nEnter first number: ")
    var num1 = scala.io.StdIn.readDouble();

    println("\nEnter second number: ")
    var num2 = scala.io.StdIn.readDouble();

    var result = num1 / num2;
    println(s"Result: $num1 / $num2 = $result")
  }
}