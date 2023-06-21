// See https://aka.ms/new-console-template for more information
Console.Write("Введите трехначное число:");
int number = Convert.ToInt32(Console.ReadLine());

int rez = 0;

rez = number / 10 % 10;

Console.Write(rez);

