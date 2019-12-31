package aoc;

import java.io.*;

public class Day03SquaresWithThreeSides {
		
	public static void main(String[] args) throws IOException {
		partOne();
		partTwo();
	}

	public static void partOne() throws IOException {
		File file = new File("./puzzle/day03.txt");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));

		String[] input = inputRaw.readLine().trim().split("\\s+");
		int cntTriangles = 0;

		while (input != null) {
			//System.out.println(input[0] + "," + input[1] + "," + input[2]);
			int[] intSides = new int[input.length];
			for (int i=0; i<input.length; i++) {
				intSides[i] = Integer.parseInt(input[i]);
			}
			Triangle triangle = new Triangle();
			triangle.setSides(intSides);

			if (triangle.isValidTriangle()) {
				cntTriangles++;
			}
			try {
				input = inputRaw.readLine().trim().split("\\s+");
				//int tester = Integer.parseInt(input[0]);
			} catch (NullPointerException e) {
				System.out.println("...finished reading input file");
				break;
			}
		
		}
		System.out.println("Result part 1: There are " + cntTriangles + " possible triangles in the list.");
		inputRaw.close();
	}

	public static void partTwo() throws IOException {
		File file = new File("./puzzle/day03.txt");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));

		String[] inputOne = inputRaw.readLine().trim().split("\\s+");
		String[] inputTwo = inputRaw.readLine().trim().split("\\s+");
		String[] inputThree = inputRaw.readLine().trim().split("\\s+");
		int cntTriangles = 0;

		while (inputOne != null) {
			//System.out.println(input[0] + "," + input[1] + "," + input[2]);
			int[] intSidesOne = new int[3];
			int[] intSidesTwo = new int[3];
			int[] intSidesThree = new int[3];
			// This is not a very good idea. This must be possible in a more elegant way like an array of array or reading everything at once?!
			intSidesOne[0] = Integer.parseInt(inputOne[0]);
			intSidesOne[1] = Integer.parseInt(inputTwo[0]);
			intSidesOne[2] = Integer.parseInt(inputThree[0]);
			intSidesTwo[0] = Integer.parseInt(inputOne[1]);
			intSidesTwo[1] = Integer.parseInt(inputTwo[1]);
			intSidesTwo[2] = Integer.parseInt(inputThree[1]);
			intSidesThree[0] = Integer.parseInt(inputOne[2]);
			intSidesThree[1] = Integer.parseInt(inputTwo[2]);
			intSidesThree[2] = Integer.parseInt(inputThree[2]);
			
			Triangle triangleOne = new Triangle();
			Triangle triangleTwo = new Triangle();
			Triangle triangleThree = new Triangle();
			triangleOne.setSides(intSidesOne);
			triangleTwo.setSides(intSidesTwo);
			triangleThree.setSides(intSidesThree);

			if (triangleOne.isValidTriangle()) {
				cntTriangles++;
			}
			if (triangleTwo.isValidTriangle()) {
				cntTriangles++;
			}
			if (triangleThree.isValidTriangle()) {
				cntTriangles++;
			}
			try {
				inputOne = inputRaw.readLine().trim().split("\\s+");
				//int tester = Integer.parseInt(input[0]);
			} catch (NullPointerException e) {
				System.out.println("...finished reading input file");
				break;
			}
			inputTwo = inputRaw.readLine().trim().split("\\s+");
			inputThree = inputRaw.readLine().trim().split("\\s+");
		
		}
		System.out.println("Result part 2: There are " + cntTriangles + " possible triangles in the list.");
		inputRaw.close();
	}

	static class Triangle {
		int[] sides = null;

		public int[] getSides() {
			return sides;
		}

		public void setSides(int[] sides) {
			this.sides = sides;
		}

		public boolean isValidTriangle() {
			if (this.sides[0]+this.sides[1] > this.sides[2] && this.sides[0]+this.sides[2] > this.sides[1] && this.sides[1]+this.sides[2] > this.sides[0]) {
				return true;
			} else {
				return false;
			}
		}
	}


}

