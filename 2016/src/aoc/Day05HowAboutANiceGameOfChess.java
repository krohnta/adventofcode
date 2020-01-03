package aoc;

import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.*;

public class Day05HowAboutANiceGameOfChess {

	public static void main(String[] args) throws NoSuchAlgorithmException {
		String doorID = "ugkcyxxp";
		partOne(doorID);
		partTwo(doorID);
	}

	public static void partOne(String doorID) throws NoSuchAlgorithmException {
		StringBuffer password = new StringBuffer("");
		long cnt = 0;
		String doorIndex = "";

		while (password.length()<8) {
			doorIndex = doorID + Long.toString(cnt);
			
			// https://stackoverflow.com/a/30119004/12155532 :
			MessageDigest md5 = MessageDigest.getInstance("MD5");
			md5.update(StandardCharsets.UTF_8.encode(doorIndex));
			String result = String.format("%032x", new BigInteger(1,md5.digest()));
			if ("00000".equals(result.substring(0,5))) {
				password.append(result.substring(5,6));
				System.out.println(password);
			}
			cnt++;
	
	
		}
		System.out.println("Result part 1: " + password);
	}

	public static void partTwo(String doorID) throws NoSuchAlgorithmException {
		StringBuffer password = new StringBuffer("--------");
		long cnt=0;
		String doorIndex = "";
		int loopCnt = 0;
		int position = 0;

		while (loopCnt < 8) {
			doorIndex = doorID + Long.toString(cnt);
			
			MessageDigest md5 = MessageDigest.getInstance("MD5");
			md5.update(StandardCharsets.UTF_8.encode(doorIndex));
			String result = String.format("%032x", new BigInteger(1,md5.digest()));
			if ("00000".equals(result.substring(0,5))) {
				try {
					position = Integer.parseInt(result.substring(5,6));
					if (position < 8 && password.substring(position,position+1).equals("-")) {
						System.out.println(position + ", password fragment: " + password);
						password.replace(position,position+1,result.substring(6,7));
						System.out.println(password);
						loopCnt++;
					}

				} catch (NumberFormatException e) {
					// nothing to do here, just skip the evaluation...
				}
			}
			cnt++;
	
	
		}
		System.out.println("Result part 2: " + password);

	}
}