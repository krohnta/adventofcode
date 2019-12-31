package aoc;

import java.io.*;

public class Day03SquaresWithThreeSides {
		
	public static void main(String[] args) throws IOException {
		partOne();
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

