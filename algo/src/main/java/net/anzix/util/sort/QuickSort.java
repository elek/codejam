package net.anzix.util.sort;

import java.util.List;

public class QuickSort implements Sort {
	public <T extends Comparable<? super T>> void sort(List<T> list) {
		sort(list, 0, list.size() - 1);
	}

	<T extends Comparable<? super T>> void sort(List<T> list, int startIndex,
			int endIndex) {
		int pivotIndex = divide(list, startIndex, endIndex);
		if (pivotIndex > 0 && pivotIndex - 1 > startIndex) {
			sort(list, startIndex, pivotIndex - 1);
		}
		if (pivotIndex < list.size() - 1 && pivotIndex + 1 < endIndex) {
			sort(list, pivotIndex + 1, endIndex);
		}
	}

	<T extends Comparable<? super T>> int divide(List<T> list, int startIndex,
			int endIndex) {
		int storeIndex = startIndex;
		T pivot = list.get(endIndex);
		for (int i = startIndex; i < endIndex; i++) {
			if (pivot.compareTo(list.get(i)) > 0) {
				T tmp = list.get(i);
				list.set(i, list.get(storeIndex));
				list.set(storeIndex, tmp);
				storeIndex++;
			}
		}
		T tmp = list.get(endIndex);
		list.set(endIndex, list.get(storeIndex));
		list.set(storeIndex, tmp);
		return storeIndex;

	}

}
