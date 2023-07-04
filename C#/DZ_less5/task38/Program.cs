// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
// [3.22, 4.2, 1.15, 77.15, 65.2] => 77.15 - 1.15 = 76


Console.WriteLine("Введите размер массива:");
int n = Convert.ToInt32(Console.ReadLine()); // Задаём размер массива
int [] mass  = new int[n];      // Создаём массив
Random rnd = new Random();      // Создание объекта для генерации чисел
for (int i = 0; i < n; i++)
    { mass[i] = rnd.Next(-50, 50);  // Заполнение рандомами
    Console.Write($" {mass[i]} ");
}
int min = 0;
int max = 0;
foreach (int i in mass)  // Поиск максимального и минимального значения
{
    if (min > i) min = i;
    if (max < i) max = i;
}
Console.WriteLine($"\n Максимальный элемент: {max}\n Минимальный элемент: {min}");
Console.WriteLine($"Разница между максимальным и минимальным элементом: {max-min}");
