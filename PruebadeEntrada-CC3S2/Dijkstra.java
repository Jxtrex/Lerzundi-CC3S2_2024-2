import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Dijkstra {
    class Arista {
        int datoDestino;
        Arista sgteArista;
        int peso;

    }

    class Vertice {
        int datoOrigen;
        Arista adyacente;
        Vertice sgteVertice;
    }

    class Grafo {
        private Vertice pGrafo;

        Grafo() {
            pGrafo = null;
        }

        void insertarVertice(int data) {
            Vertice p;
            p = new Vertice();
            p.datoOrigen = data;
            p.adyacente = null;
            p.sgteVertice = pGrafo;
            pGrafo = p;
        }

        void insertarArista(int x, int y, int weight) {
            Vertice p;
            Arista a;
            p = pGrafo;
            if (p != null) {
                while (p.datoOrigen != x && p != null) {
                    p = p.sgteVertice;
                }
                if (p != null) {
                    a = new Arista();
                    a.peso = weight;
                    a.datoDestino = y;
                    a.sgteArista = p.adyacente;
                    p.adyacente = a;
                }
            }
        }

        void imprimirGrafo() {
            Vertice p;
            Arista a;
            p = pGrafo;
            if (p == null) {
                System.out.println("Grafo vacio");
            } else {
                while (p != null) {
                    System.out.print(p.datoOrigen + ":");
                    a = p.adyacente;
                    while (a != null) {
                        System.out.print(a.datoDestino + "->");
                        a = a.sgteArista;
                    }

                    int[] respuesta = vecinosdeP(p.datoOrigen);
                    int k = 0;

                    while (respuesta[k] != -1) {
                        System.out.print(respuesta[k++] + "->");
                    }
                    System.out.println();
                    p = p.sgteVertice;
                }
            }
        }

        int[] vecinosdeP(int vertice) {
            Vertice ptemp = pGrafo;
            Arista atemp;
            int partida = vertice;

            int[] respuesta={};

            int cont = 0;
            while (ptemp != null) {
                atemp = ptemp.adyacente;
                int llegada;
                while (atemp != null) {
                    llegada = atemp.datoDestino;
                    if (llegada == partida) {
                        respuesta[cont] = ptemp.datoOrigen;
                        cont++;
                        respuesta[cont] = -1;
                        break;
                    }
                    atemp = atemp.sgteArista;
                }
                ptemp = ptemp.sgteVertice;

                if (ptemp == null) {
                    break;
                } else if (ptemp.datoOrigen == partida) {
                    ptemp = ptemp.sgteVertice;
                }
            }
            return respuesta;
        }

        
    }

    void AlgoritmoDijkstra(Grafo grafo,int verticeInicio) {
        System.out.println("Ejecutando Algoritmo de Dijkstra desde el vértice ("+verticeInicio+")");

        // Vértice inicial
        int V = 0;
        Vertice temp = grafo.pGrafo;
        while(temp != null){
            temp = temp.sgteVertice;
            V++;
        }

        // Aristas en Graph
        int[][] graph = new int[V][V];
        temp = grafo.pGrafo;
        Arista atemp;
        while(temp != null){
            atemp = temp.adyacente;
            while(atemp!=null){
                graph[temp.datoOrigen][atemp.datoDestino] = atemp.peso;
                graph[atemp.datoDestino][temp.datoOrigen] = atemp.peso;
                atemp = atemp.sgteArista;
            }
            temp = temp.sgteVertice;
        }

        // Algoritmo

        int[] parent = new int[V];
        int[] rank = new int[V];

        for (int node = 0; node < V; node++) {
            parent[node] = node;
            rank[node] = 0;
        }

        int[] distancias = new int[V];
        boolean[] verticesVisitados =  new boolean[V];
        for (int i = 0; i < V; i++) {
            distancias[i] = Integer.MAX_VALUE;
            verticesVisitados[i] = false;
        }

        distancias[verticeInicio] = 0;

        for (int i = 0; i < V-1; i++) {
            int min = distanciasMinAdyacentes(distancias, verticesVisitados, V);

            verticesVisitados[min] = true;
            for (int w = 0; w < V; w++) {
                if(!verticesVisitados[w] 
                && graph[min][w] != 0
                && distancias[min] != Integer.MAX_VALUE
                && distancias[min] + graph[min][w] < distancias[w])
                {
                    distancias[w] = distancias[min] + graph[min][w];
                }
            }
        }

        int pesoTotal = 0;
        for (int k = 0; k < V; k++) {
            pesoTotal += distancias[k];
            System.out.printf("V[%i] --- V[%i] = %i",verticeInicio, k, distancias[k]);
            System.out.println();
        }
        System.out.printf("Peso total = %i\n", pesoTotal);
    }

    int find(int[] parent, int i) {
        if (parent[i] == i) {
            return i;
        }
        return find(parent, parent[i]);
    }

    void unionSet(int[] parent, int[] rank, int x, int y) {
        int xroot = find(parent, x);
        int yroot = find(parent, y);

        if (rank[xroot] < rank[yroot]) {
            parent[xroot] = yroot;
        } else if (rank[xroot] > rank[yroot]) {
            parent[yroot] = xroot;
        } else {
            parent[yroot] = xroot;
            rank[xroot]++;
        }
    }

    int distanciasMinAdyacentes(int[] distancias, boolean[] verticesVisitados, int V)
    {
        int min = Integer.MAX_VALUE;
        int minIndex = 0;

        for (int i = 0; i < V; i++) {
            if(verticesVisitados[i] == false && distancias[i] <= min){
                min = distancias[i];
                minIndex = i;
            };
        }
        
        return minIndex;
    }


    public static void main(String[] args) {
        Dijkstra dijkstra = new Dijkstra();
        Grafo g = dijkstra.new Grafo();

        g.insertarVertice(0);
        g.insertarVertice(1);
        g.insertarVertice(2);
        g.insertarVertice(3);
        g.insertarVertice(4);
        g.insertarVertice(5);

        g.insertarArista(0, 1, 41);
        g.insertarArista(1, 2, 51);
        g.insertarArista(2, 3, 50);
        g.insertarArista(4, 3, 36);
        g.insertarArista(3, 5, 38);
        g.insertarArista(3, 0, 45);
        g.insertarArista(0, 5, 29);
        g.insertarArista(5, 4, 21);
        g.insertarArista(1, 4, 32);
        g.insertarArista(4, 2, 32);
        g.insertarArista(5, 1, 24);

        // Main
        System.out.println("Vertices||Aristas");
        g.imprimirGrafo();

        System.out.print("Elija el vértice para comenzar el Algoritmo de Dijkstra: ");

        Scanner scn = new Scanner(System.in);
        int verticeInicio = scn.nextInt();
        dijkstra.AlgoritmoDijkstra(g, verticeInicio);
    }
}