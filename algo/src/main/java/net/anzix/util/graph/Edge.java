package net.anzix.util.graph;

public class Edge<V> {
	
	
	public Edge(V value) {
		super();
		this.value = value;
	}

	public V getValue() {
		return value;
	}

	public void setValue(V value) {
		this.value = value;
	}

	private V value;

}
