package net.anzix.util.sort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import junit.framework.Assert;

import org.junit.Test;

public class SortTest {
	@Test
	public void randomizedSort() {
		List<Sort> sorts = new ArrayList<Sort>();
		sorts.add(new QuickSort());
		sorts.add(new BubbleSort());

		for (Sort sort : sorts) {
			for (int t = 0; t < 10; t++) {
				List<Integer> orig = new ArrayList<Integer>();
				for (int i = 0; i < 50; i++) {
					orig.add((int) Math.round(Math.random() * 1000));
				}
				List<Integer> contra = new ArrayList<Integer>(orig);

				sort.sort(orig);
				Collections.sort(contra);

				Assert.assertEquals("error in "+sort.getClass(),contra, orig);
			}

		}

	}

}
