// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.

Console.WriteLine("введите число");
int i = Convert.ToInt32(Console.ReadLine());
int sum = 0;

while (i > 0)
{
int num = i % 10;
i /= 10;
sum += num;
}
Console.WriteLine("сумма всех цифр в числе равна: " + sum);