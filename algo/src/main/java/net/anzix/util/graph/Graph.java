package net.anzix.util.graph;

import java.util.Collection;

public interface Graph<N, E> {
	public Collection<N> getAllNodes();

	public Collection<N> getNeighbourNodes(N node);

	public Collection<E> getEdgesFrom(N node);

	public Collection<E> getEdgesTo(N node);

	public void addEdge(N start, N end, E edge);

	public void addNode(N node);

	public N getStart(E edge);

	public N getEnd(E edge);

}
