package aoc;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Day01NoTimeForATaxicab {
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

		// part 2 requires storing the whole path
		List<String> locations = new ArrayList<String>();
		for (int i=0; i<input.length; i++) {
			char direction = input[i].charAt(0);
			int steps = Integer.parseInt(input[i].substring(1));
			facing = newFacing(facing, direction);
			switch (facing) {
				case 0 : for (int j=0; j<steps; j++) {
							locations.add(Integer.toString(x+j) + "," + Integer.toString(y));
						}
						x += steps;
						break;
				case 1 : for (int j=0; j<steps; j++) {
							locations.add(Integer.toString(x) + "," + Integer.toString(y+j));
						}
						y += steps; 
						break;
				case 2 : for (int j=0; j<steps; j++) {
							locations.add(Integer.toString(x-j) + "," + Integer.toString(y));
						}
						x -= steps; 
						break;
				case 3 : for (int j=0; j<steps; j++) {
							locations.add(Integer.toString(x) + "," + Integer.toString(y-j));
						}
						y -= steps; 
						break;
			}
			/* DEBUG OUTPUT 
			 * System.out.println("Last walk: " + direction + steps + ", current location: (" + x + "," + y + "), current facing: " + facing);
			 */
		}

		// calculate solution for part 1:
		int resultPart1 = Math.abs(x) + Math.abs(y);
		System.out.println("Final location for part 1: (" + x + "," + y + "), distance to (0,0): " + resultPart1);

		// calculate solution for part 2:
		for (int i=0; i<locations.size(); i++) {
			String compare = locations.get(i);
			for (int j=i+1; j<locations.size(); j++) {
				if (locations.get(j).equals(compare)) {
					String[] resultPart2Raw = compare.split(",");
					int resultPart2 = Math.abs(Integer.parseInt(resultPart2Raw[0])) + Math.abs(Integer.parseInt(resultPart2Raw[1]));
					System.out.println("First path crossing for part 2 found at (" + compare + "), distance to (0,0): " + resultPart2);
					System.exit(0);
				}
			}
		}


		inputRaw.close();
	}
}