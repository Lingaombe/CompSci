/*
 * Write a java program to create 10 questions array with another to store its correct answer. 
Answer array will be the integer array. Display the questions from the array and accept the 
answers from the user. At the end of all questions display the result for user. (Marking 
scheme as 1 mark for 1 right answer)
 */

import java.util.Scanner;

public class ArraysExams {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Questions array
        String[] questions = {
            "1. What is 2 + 2?",
            "2. What is 5 * 3?",
            "3. What is 10 - 7?",
            "4. What is 15 / 3?",
            "5. What is the square of 6?",
            "6. What is 20 % 3?",
            "7. What is 12 + 8?",
            "8. What is 7 * 7?",
            "9. What is 100 / 25?",
            "10. What is 9 - 4?"
        };

        // Correct answers
        int[] correctAnswers = {4, 15, 3, 5, 36, 2, 20, 49, 4, 5};

        // User answers
        int[] userAnswers = new int[questions.length];

        int score = 0;

        // Asking questions
        System.out.println("---- Quiz Start ----");
        for (int i = 0; i < questions.length; i++) {
            System.out.println(questions[i]);
            System.out.print("Your Answer: ");
            userAnswers[i] = sc.nextInt();

            // Check correctness
            if (userAnswers[i] == correctAnswers[i]) {
                score++;
            }
        }

        // Display result
        System.out.println("\n---- Quiz Over ----");
        System.out.println("Your total score: " + score + " out of " + questions.length);

        // Optionally, show correct vs user answers
        System.out.println("\nReview:");
        for (int i = 0; i < questions.length; i++) {
            System.out.println(questions[i]);
            System.out.println("Your Answer: " + userAnswers[i] + 
                               " | Correct Answer: " + correctAnswers[i]);
        }

        sc.close();
    }
}
