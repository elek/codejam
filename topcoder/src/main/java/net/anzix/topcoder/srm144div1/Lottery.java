package net.anzix.topcoder.srm144div1;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Lottery {
	Map<Integer, BigDecimal> factCash = new HashMap();
	Map<Tuple, BigDecimal> cash = new HashMap();

	public String[] sortByOdds(String[] rules) {
		Map<BigDecimal, List<String>> odds = new TreeMap<BigDecimal, List<String>>();
		for (String rule : rules) {
			String[] p = rule.split(":");
			String[] v = p[1].trim().split(" ");
			try {
				BigDecimal tiNo = noOfTickets(Integer.parseInt(v[0]),
						Integer.parseInt(v[1]),
						v[2].equalsIgnoreCase("t") ? true : false,
						v[3].equalsIgnoreCase("t") ? true : false);
				if (odds.get(tiNo) == null) {
					odds.put(tiNo, new ArrayList());
				}
				odds.get(tiNo).add(p[0]);
			} catch (Exception ex) {
				System.out.println("Error on calculacing " + rule);
				ex.printStackTrace();
			}

		}

		List<String> result = new ArrayList();
		for (BigDecimal l : odds.keySet()) {
			List<String> s = odds.get(l);
			Collections.sort(s);
			for (String n : s) {
				result.add(n);
			}
		}
		return result.toArray(new String[0]);

	}

	public BigDecimal sortedNotUnique(int choices, int blanks) {
		Tuple t = new Tuple(choices, blanks);
		if (cash.get(t) != null) {
			return cash.get(t);
		}
		if (blanks == 1) {
			return BigDecimal.valueOf(choices);
		}
		BigDecimal res = BigDecimal.ZERO;
		for (int i = 1; i <= choices; i++) {
			res  = res.add(sortedNotUnique(i, blanks - 1));
		}
		cash.put(t, res);
		return res;
	}

	public BigDecimal noOfTickets(int choices, int blanks, boolean sorted,
			boolean unique) {
		if (!sorted && !unique) {
			return BigDecimal.valueOf(Math.pow(choices, blanks));
		} else if (sorted && !unique) {
			return sortedNotUnique(choices, blanks);
		} else if (!sorted && unique) {
			return fact(choices).divide(fact(choices - blanks));
		} else if (sorted && unique) {
			return fact(choices).divide(fact(blanks)).divide(fact(choices - blanks));

		}
		return null;

	}

	BigDecimal fact(int f) {
		if (factCash.get(f) != null) {
			return factCash.get(f);
		}
		BigDecimal v = BigDecimal.ONE;
		for (int i = 1; i <= f; i++) {
			v = v.multiply(BigDecimal.valueOf(i));
		}
		factCash.put(f, v);
		return v;
	}

	private static class Tuple {
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + a;
			result = prime * result + b;
			return result;
		}

		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Tuple other = (Tuple) obj;
			if (a != other.a)
				return false;
			if (b != other.b)
				return false;
			return true;
		}

		int a;
		int b;

		public Tuple(int a, int b) {
			this.a = a;
			this.b = b;
		}

	}
}
