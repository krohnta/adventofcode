package aoc;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class Day06SignalsAndNoise {
	public static void main(String[] args) throws IOException {

		File file = new File("./puzzle/day06.txt");
		//File file = new File("./puzzle/day06test.txt");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));

		String input = inputRaw.readLine();
		int l = input.length();
		int lines = 1;

		Map<String, Integer> countCommons = new HashMap<String, Integer>();
		
		while (input != null) {
			/* Go through the input and count all occurrences of a character,
			 * divide the count to the "columns" by adding the column number
			 * to the key, i.e. the key c is "character" + "column number".
			 */
			for (int i=0; i<input.length(); i++) {
				String c = input.substring(i,i+1) + Integer.toString(i);
				if (countCommons.containsKey(c)) {
					countCommons.put(c, countCommons.get(c)+1);
				} else {
					countCommons.put(c, 1);
				}
			}

			try {
				input = inputRaw.readLine();
				lines++;
			} catch (NullPointerException e) {
				System.out.println("...finished reading input file");
				break;
			}
		}

		StringBuffer resultPartOne = new StringBuffer(l);
		StringBuffer resultPartTwo = new StringBuffer(l);

		/* Find min and max amount of occurring characters and append their respective
		 * character in the key to the result.
		 * I'm quite proud that I was able to 'refactor' my solution for part 1 within
		 * SIX MINUTES to get the correct solution for part 2. With a test run on the
		 * day06test.txt data.
		 */
		for (int i=0; i<l; i++) {
			int maxi = 0;
			int mini = lines;
			String maxiS = "";
			String miniS = "";
			for (char c='a'; c<='z'; c++) {
				String key = Character.toString(c) + Integer.toString(i);
				if (countCommons.containsKey(key)) {
					if (countCommons.get(key) > maxi) {
						maxiS = Character.toString(c);
						maxi = countCommons.get(key);
					}
					if (countCommons.get(key) < mini) {
						miniS = Character.toString(c);
						mini = countCommons.get(key);
					}
				}
			}
			resultPartOne = resultPartOne.append(maxiS);
			resultPartTwo = resultPartTwo.append(miniS);
		}

		System.out.println("Result part 1: " + resultPartOne);
		System.out.println("Result part 2: " + resultPartTwo);

		inputRaw.close();
	}
}