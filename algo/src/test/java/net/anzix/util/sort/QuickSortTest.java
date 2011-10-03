package net.anzix.util.sort;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import junit.framework.Assert;

import org.junit.Test;

public class QuickSortTest {

	
	@Test
	public void sort() {
		List<Integer> list = i(5, 4, 1, 2, 3);
		new QuickSort().sort(list);
		Assert.assertEquals(i(1, 2, 3, 4, 5), list);

	}

	@Test
	public void divide() {
		List<Integer> list = i(5, 4, 1, 2, 3);
		int sort = new QuickSort().divide(list, 0, list.size() - 1);
		Assert.assertEquals(2, sort);
		Assert.assertEquals(i(1, 2, 3, 4, 5), list);

		list = i(5, 4, 1, 2, 3);
		sort = new QuickSort().divide(list, 0, 2);
		Assert.assertEquals(0, sort);
		Assert.assertEquals(i(1, 4, 5, 2, 3), list);
	}

	private List<Integer> i(Integer... values) {
		return Arrays.asList(values);
	}
}