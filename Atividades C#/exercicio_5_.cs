Console.WriteLine("Numéro da peça: Quantidade: Preço unitário:");
string [] peca_1 = Console.ReadLine().Split(" ");
double valor_total;

int number_piece1 = int.Parse(peca_1[0]);
int quantity_piece1 = int.Parse(peca_1[1]);
int value_piece1 = int.Parse(peca_1[2]);

Console.WriteLine("Numéro da peça: Quantidade: Preço unitário:");
string [] peca_2 = Console.ReadLine().Split(" ");
int number_piece2 = int.Parse(peca_2[0]);
int quantity_piece2 = int.Parse(peca_2[1]);
int value_piece2 = int.Parse(peca_2[2]);


valor_total = (value_piece1 * quantity_piece1) + (value_piece2 * quantity_piece2);


Console.WriteLine($"Valor a pagar: R$ {valor_total} \nSeus respectivos códigos: Peça 1 - {number_piece1} Peça 2 - {number_piece2}");
