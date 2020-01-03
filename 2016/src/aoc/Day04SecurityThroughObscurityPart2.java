package aoc;

import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import aoc.Day04SecurityThroughObscurityPart1.Room;


public class Day04SecurityThroughObscurityPart2 {
	
	public static void main(String[] args) throws IOException {

		File file = new File("./puzzle/day04.txt");
		String check = new String("north");
		//File file = new File("./puzzle/day04test.txt");
		//String check = new String("very");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));
		String input = inputRaw.readLine();

		while (input != null) {
			Room room = new Room();
			Pattern pattern = Pattern.compile("(.*)([0-9]{3}).([a-z]{5}).");
			Matcher matcher = pattern.matcher(input);
			/* It is necessary to run matcher.find() before the groups can be used in
			 * the setters. The output of matcher.find() is true for all of my input. Yay \o/
			 */
			matcher.find();
			room.setEncryptedName(matcher.group(1).replaceAll("-",""));
			room.setSectorID(Integer.parseInt(matcher.group(2))%26);
			StringBuffer decryptedName = new StringBuffer(room.getEncryptedName().length());
			char c;
			char offset;

			for (int i=0; i<room.getEncryptedName().length(); i++) {
				c = room.getEncryptedName().charAt(i);
				offset = (char)room.getSectorID();
				if (c+offset > 'z') {
					decryptedName.append(Character.toString(c+offset-26));
				} else {
					decryptedName.append(Character.toString(c+offset));
				}
			}

			if (decryptedName.toString().substring(0,check.length()).equals(check)) {
				System.out.println(decryptedName);
				System.out.println(room.getEncryptedName());
				System.out.println("Result part 2: North pole objects are stored in room no " + matcher.group(2));
				// No need to look any further, so do a clean exit:
				System.exit(0);
			}


			try {
				input = inputRaw.readLine();
			} catch (NullPointerException e) {
				System.out.println("...finished reading input file");
				break;
			}
		}


		inputRaw.close();
	}
}