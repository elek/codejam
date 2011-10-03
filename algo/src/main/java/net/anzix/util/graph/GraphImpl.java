package net.anzix.util.graph;

import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class GraphImpl<N,E> implements Graph<N,E>{
	private Map<E,N> endNodes = new HashMap<E, N>();
	private Map<E,N> startNodes = new HashMap<E, N>();
	private Map<N,List<E>> edgesFrom = new HashMap();
	private Map<N,List<E>> edgesTo = new HashMap();
	@Override
	public Collection<N> getAllNodes() {

	}

	@Override
	public Collection<N> getNeighbourNodes(N node) {
		Set<N> result = new HashSet();
		for (E e : edgesFrom.get(node)){
			result.add(e);
		}
		return result;
	}

	@Override
	public Collection<E> getEdgesFrom(N node) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Collection<E> getEdgesTo(N node) {
		// TODO Auto-generated method stub
		return null;
	}
	

	@Override
	public N getEnd(E edge) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void addEdge(N start, N end, E edge) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void addNode(N node) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public N getStart(E edge) {
		// TODO Auto-generated method stub
		return null;
	}

}
