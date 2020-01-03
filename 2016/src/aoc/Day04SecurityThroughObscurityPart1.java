package aoc;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Day04SecurityThroughObscurityPart1 {
	
	public static void main(String[] args) throws IOException {

		File file = new File("./puzzle/day04.txt");
		//File file = new File("./puzzle/day04test.txt");
		BufferedReader inputRaw = new BufferedReader(new FileReader(file));

		String input = inputRaw.readLine();
		int sumOfSectorIDs = 0;

		// create a lookup array for a-z, so alphabet[0]=='a', alphabet[25]=='z'
		Character[] alphabet = new Character[26];
		int j = 0;
		for (char c='a'; c<='z'; c++) {
			alphabet[j] = c;
			j++;
		}

		while (input != null) {
			Room room = new Room();
			Pattern pattern = Pattern.compile("(.*)([0-9]{3}).([a-z]{5}).");
			Matcher matcher = pattern.matcher(input);
			/* It is necessary to run matcher.find() before the groups can be used in
			 * the setters. The output of matcher.find() is true for all of my input. Yay \o/
			 */
			matcher.find();
			room.setEncryptedName(matcher.group(1).replaceAll("-",""));
			room.setSectorID(Integer.parseInt(matcher.group(2)));
			room.setChecksum(matcher.group(3));
			//System.out.println(room.getEncryptedName());
			
			Integer[] cnt = new Integer[26];
			Integer[] cntCopy = new Integer[26];
			Arrays.fill(cnt, 0);
			Arrays.fill(cntCopy, 0);
			int posInAlphabet = 0;
			for (int i=0; i<room.getEncryptedName().length(); i++) {
				// check for each char in encryptedName the position in alphabet and add 1 for each occurrence
				posInAlphabet = Arrays.asList(alphabet).indexOf(room.getEncryptedName().charAt(i));
				cnt[posInAlphabet]++;
				cntCopy[posInAlphabet]++;
			}

			// find 5 largest ints in cnt and append their respective character value to calculate the checksum
			Arrays.sort(cnt, Collections.reverseOrder());
			StringBuffer calcChecksumDuplicate = new StringBuffer();

			for (int k=0; k<5; k++) {
				calcChecksumDuplicate = appendChar(cnt[k], calcChecksumDuplicate, cntCopy, alphabet);
			}

			// make the calculated checksum a String[] of unique characters
			String[] calcChecksum = new String[5];
			j=0;
			for (int i=0; i<calcChecksumDuplicate.length(); i++) {
				if (!Arrays.asList(calcChecksum).contains(calcChecksumDuplicate.substring(i,i+1))) {
					calcChecksum[j] = calcChecksumDuplicate.substring(i,i+1);
					j++;
				}
				if (j>4) {
					break;
				}
			}

			// and FINALLY make the String[] a String
			String str = "";
			for (int i=0; i<calcChecksum.length; i++) {
				str += calcChecksum[i];
			}

			if (room.isValidRoom(str)) {
				sumOfSectorIDs += room.getSectorID();
			}

			try {
				input = inputRaw.readLine();
			} catch (NullPointerException e) {
				System.out.println("...finished reading input file");
				break;
			}

		}
		System.out.println("Result part 1: The sum of checksums for valid rooms is " + sumOfSectorIDs);

		inputRaw.close();
	}

	public static StringBuffer appendChar(int checkValue, StringBuffer str, Integer[] cntCopy, Character[] alphabet) {
		for (int i=0; i<26; i++) {
			if (cntCopy[i] == checkValue) {
				str.append(Character.toString(alphabet[i]));
			}
		}
		return str;

	}


	static class Room {
		String encryptedName = "";
		int sectorID = 0;
		String checksum = "";

		public String getEncryptedName() {
			return encryptedName;
		}

		public void setEncryptedName(String encryptedName) {
			this.encryptedName = encryptedName;
		}

		public int getSectorID() {
			return sectorID;
		}

		public void setSectorID(int sectorID) {
			this.sectorID = sectorID;
		}

		public String getChecksum() {
			return checksum;
		}

		public void setChecksum(String checksum) {
			this.checksum = checksum;
		}

		public boolean isValidRoom(String calculatedChecksum) {
			return calculatedChecksum.equals(this.checksum);
		}
	}
}