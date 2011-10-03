package net.anzix.topcoder.srm144div1;

import org.junit.Assert;

import org.junit.Test;

public class LotteryTest {
	@Test
	public void test2() {
		Lottery l = new Lottery();
		String[] inp1 = new String[] { "PICK ANY TWO: 10 2 F F",
				"PICK TWO IN ORDER: 10 2 T F", "PICK TWO DIFFERENT: 10 2 F T",
				"PICK TWO LIMITED: 10 2 T T" };

		String[] res1 = new String[] { "PICK TWO LIMITED", "PICK TWO IN ORDER",
				"PICK TWO DIFFERENT", "PICK ANY TWO" };

		String[] in2 = new String[] { "INDIGO: 93 8 T F", "ORANGE: 29 8 F T",
				"VIOLET: 76 6 F F", "BLUE: 100 8 T T", "RED: 99 8 T T",
				"GREEN: 78 6 F T", "YELLOW: 75 6 F F" };
		String[] res2 = new String[] { "RED", "ORANGE", "YELLOW", "GREEN",
				"BLUE", "INDIGO", "VIOLET" };

		Assert.assertArrayEquals(res1, l.sortByOdds(inp1));
		Assert.assertArrayEquals(res2, l.sortByOdds(in2));

	}

	@Test
	public void test1() {
		Lottery l = new Lottery();
		Assert.assertEquals(100, l.noOfTickets(10, 2, false, false).intValue());
		Assert.assertEquals(45, l.noOfTickets(10, 2, true, true).intValue());
		Assert.assertEquals(90, l.noOfTickets(10, 2, false, true).intValue());
		Assert.assertEquals(55, l.noOfTickets(10, 2, true, false).intValue());
		Assert.assertEquals(186087894300l, l.noOfTickets(93, 8, true, false).longValue());

	}
}
