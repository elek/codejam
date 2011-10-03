package net.anzix.util.sort;

import java.util.List;

public class BubbleSort implements Sort {
	public <T extends Comparable<? super T>> void sort(List<T> list) {
		for (int j = 0; j < list.size(); j++) {
			for (int i = 0; i < list.size() - 1; i++) {
				T a = list.get(i);
				T b = list.get(i + 1);
				if (a.compareTo(b) > 0) {
					list.set(i, b);
					list.set(i + 1, a);
				}
			}
		}
	}
}
