

Console.WriteLine("Digite a largura do array:");
int largura = int.Parse(Console.ReadLine());

int[] vect = new int [largura];


for(int i = 0; i < largura; i++)
{
    System.Console.WriteLine($"Digite o {i+1} valor:");

    vect[i] = int.Parse(Console.ReadLine());

}

int[] ordenacao = new int [largura];

for (int i = 0; i < largura ; i++)
{
    ordenacao[i] = vect[i];
}


for (int i = 0; i < largura - 1; i++)
{
    for (int j = 0; j< largura - 1 - i; j++)
    {
        if(ordenacao[j]> ordenacao[j + 1])
        {
            int aux = ordenacao[j];
            ordenacao[j] = ordenacao[j+1];
            ordenacao[j+1] = aux;

        }
    }
}


for (int i = 0; i < largura ; i++)
{
Console.WriteLine($"Vetor 1 sem ordenação: {vect[i]}");
Console.WriteLine();
Console.WriteLine();
}


for (int i = 0; i < largura ; i++)
{
Console.WriteLine($"Vetor 2 com ordenação: {ordenacao[i]}");
}



