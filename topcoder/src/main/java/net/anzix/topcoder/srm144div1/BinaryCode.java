package net.anzix.topcoder.srm144div1;

public class BinaryCode {
	public String[] decode(String message) {

		return new String[] { decode(message, '0'), decode(message, '1') };
	}

	String decode(String message, char firstChar) {
		String msg = message;
		String orig = "0" + firstChar;
		for (int i = 2; i <= message.length(); i++) {
			int v = msg.charAt(i - 2)
					- (orig.charAt(i - 1) + orig.charAt(i - 2)) + 48;
			if (v > 1)
				return "NONE";
			orig += "" + v;
		}
		int last = orig.charAt(orig.length() - 1)
				+ orig.charAt(orig.length() - 2) - 2 * 48;
		if (last != (msg.charAt(message.length() - 1) - 48)) {
			return "NONE";
		}

		return orig.substring(1);
	}
}
