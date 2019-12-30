package aoc;

import java.io.*;

public class Day02BathroomSecurityPart1 {

	public static int[] nextButton(int[] currentButton, char direction) {
		int[] next = currentButton;
		/* "lookup-table":
		 * 1 = (0,0)
		 * 2 = (0,1)
		 * 3 = (0,2)
		 * 4 = (1,0)
		 * 5 = (1,1)
		 * 6 = (1,2)
		 * 7 = (2,0)
		 * 8 = (2,1)
		 * 9 = (2,2)
		 *   => l = (x,y--), r = (x,y++), u = (x--,y), d = (x++,y)
		 *   => re-transformation: (x,y) <=> 3*x+y+1
		 */

		switch (direction) {
			case 'L' : { if (next[1]-1 >= 0) {next[1]--;}; break; }
			case 'R' : { if (next[1]+1 <= 2) {next[1]++;}; break; }
			case 'U' : { if (next[0]-1 >= 0) {next[0]--;}; break; }
			case 'D' : { if (next[0]+1 <= 2) {next[0]++;}; break; }
		}
		return next;
	}


	public static void main(String[] args) throws IOException {

		File file = new File("./puzzle/day02.txt");
		//File file = new File("./puzzle/day02test.txt");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));

		// initialize start button
		int[] button = new int[2];
		button[0] = 1;
		button[1] = 1;

		/* I'm aware that it is not the best idea to hard-code the number of
		 * lines in the file to be read, however, it is sufficient for this
		 * puzzle to be solved. And yes, of course, this got me on my first
		 * attempt when switching from test data to the real input *sigh*
		 */
		for (int i=0; i<5; i++) {
			String input = inputRaw.readLine();
			for (int j=0; j<input.length(); j++) {
				char c = input.charAt(j);
				button = nextButton(button,c);
			}
			// transform coordinates to keypad value
			System.out.println(button[0]*3 + button[1] + 1);
		}
		inputRaw.close();
	}

}
