package aoc;

import java.io.*;

public class Day02BathroomSecurityPart2 {

	public static int[] nextButton(int[] currentButton, char direction) {
		int[] next = currentButton;
		/* "lookup-table":
		 * 1 = (0,2)
		 * 2 = (-1,1)
		 * 3 = (0,1)
		 * 4 = (1,1)
		 * 5 = (-2,0)
		 * 6 = (-1,0)
		 * 7 = (0,0)
		 * 8 = (1,0)
		 * 9 = (2,0)
		 * A = (-1,-1)
		 * B = (0,-1)
		 * C = (1,-1)
		 * D = (0,-2)
		 *   => l = (x--,y), r = (x++,y), u = (x,y++), d = (x,y--)
		 *   => invalid buttons have (Math.abs(x)+Math.abs(y) > 2)
		 *   => re-transformation will be a little bit more complicated
		 */

		switch (direction) {
			case 'L' : {
				boolean isValidButton = (Math.abs(currentButton[0]-1) + Math.abs(currentButton[1]) <= 2);
				if (isValidButton) {
					next[0]--;
				}
				break; }
			case 'R' : { 
				boolean isValidButton = (Math.abs(currentButton[0]+1) + Math.abs(currentButton[1]) <= 2);
				if (isValidButton) {
					next[0]++;
				}
				break; }
			case 'U' : {
				boolean isValidButton = (Math.abs(currentButton[0]) + Math.abs(currentButton[1]+1) <= 2);
				 if (isValidButton) {
					 next[1]++;
				}
				break; }
			case 'D' : {
				boolean isValidButton = (Math.abs(currentButton[0]) + Math.abs(currentButton[1]-1) <= 2);
				 if (isValidButton) {
					 next[1]--;
				}
				break; }
		}
		//System.out.print("(" + next[0] + "," + next[1] + "), ");
		return next;
	}


	public static void main(String[] args) throws IOException {

		File file = new File("./puzzle/day02.txt");
		int lines = 5;
		//File file = new File("./puzzle/day02test.txt");
		//int lines = 4;
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));

		// initialize start button
		int[] button = new int[2];
		button[0] = -2;
		button[1] = 0;

		/* I'm aware that it is not the best idea to hard-code the number of
		 * lines in the file to be read, however, it is sufficient for this
		 * puzzle to be solved. And yes, of course, this got me on my first
		 * attempt when switching from test data to the real input *sigh*
		 */
		for (int i=0; i<lines; i++) {
			String input = inputRaw.readLine();
			for (int j=0; j<input.length(); j++) {
				char c = input.charAt(j);
				button = nextButton(button,c);
			}
			// transform coordinates to keypad value
			//System.out.println(button[0]*3 + button[1] + 1);
			System.out.println(button[0] + "," + button[1]);
		}
		inputRaw.close();
	}

}
