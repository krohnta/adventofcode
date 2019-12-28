package aoc;

import java.io.*;

public class Day01 {
	public static int newFacing(int oldFacing, char newDirection) {
		int result;
		if (newDirection == 'L') {
			result = (oldFacing+3)%4;
		} else { // if (newDirection == 'R')
			result = (oldFacing+1)%4;
		}
		return result;
	}

	public static void main(String[] args) throws Exception {

		File file = new File("./puzzle/day01.txt");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));
		String[] input = inputRaw.readLine().split(", ");

		// declare and initiate start values
		int x = 0;
		int y = 0;
		/* it seems more convenient to transform N==0, E==1, S==2, W==3
		 * into the new direction instead of transitioning between 
		 * N/S/E/W as characters
		 */
		int facing = 3;

		// the following has to be done with a loop over the whole input
		for (int i=0; i<input.length; i++) {
			char direction = input[i].charAt(0);
			int steps = Integer.parseInt(input[i].substring(1));
			facing = newFacing(facing, direction);
			switch (facing) {
				case 0 : x += steps; break;
				case 1 : y += steps; break;
				case 2 : x -= steps; break;
				case 3 : y -= steps; break;
			}
			System.out.println("Last walk: " + direction + steps + ", current location: (" + x + "," + y + "), current facing: " + facing);
		}
		System.out.println(Math.abs(x) + Math.abs(y));


		//System.out.print(input[0] + "," + direction + "," + steps + ", newFacing " + newFacing(facing, direction));


		inputRaw.close();
	}
}