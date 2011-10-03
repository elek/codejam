package net.anzix.topcoder.srm144div1;

import org.junit.Assert;
import org.junit.Test;

public class BinaryCodeTest {

	@Test
	public void defaultTests() {
		BinaryCode bc = new BinaryCode();

		Assert.assertArrayEquals(new String[] { "NONE", "NONE" },
				bc.decode("123210120"));

		Assert.assertArrayEquals(new String[] { "011100011", "NONE" },
				bc.decode("123210122"));

		Assert.assertArrayEquals(new String[] { "NONE", "11001" },
				bc.decode("22111"));

		Assert.assertArrayEquals(new String[] { "NONE", "11001" },
				bc.decode("22111"));

		Assert.assertArrayEquals(new String[] { "NONE", "11001" },
				bc.decode("22111"));

		Assert.assertArrayEquals(new String[] { "NONE", "NONE" },
				bc.decode("3"));

		Assert.assertArrayEquals(new String[] {
				"01101001101101001101001001001101001",
				"10110010110110010110010010010110010" },
				bc.decode("12221112222221112221111111112221111"));

	}
}
