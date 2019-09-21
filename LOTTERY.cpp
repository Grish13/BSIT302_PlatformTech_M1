#include <iostream>
#include <iostream>
#include <iomanip>
#include <ctime>
#include <fstream>
#include <cstdlib>

using namespace std;

int Num1 = 0;
int Num2 = 0;
int Num3 = 0;
int Num4 = 0;
int Num5 = 0;
int Num6 = 0;

void SortNumbers();
void PrintToFile();

int main()
{
    srand(time(0));
    int count = 0;

    for(;;)
    {
        cout << "How many Lottery threads you want ";
        cin >> count;
        cout << endl;
        if(count)
        {
            for(int i = 1; i <= count; i++)
            {
                Num1 = rand() % (55 - 1 + 1) + 1;

                do
                {
                    Num2 = rand() % (55 - 1 + 1) + 1;
                }while(Num2 == Num1);

                do
                {
                    Num3 = rand() % (55 - 1 + 1) + 1;
                }while(Num3 == Num2 || Num3 == Num1);

                do
                {
                    Num4 = rand() % (55 - 1 + 1) + 1;
                }while(Num4 == Num3 || Num4 == Num2 || Num4 == Num1);

                do
                {
                    Num5 = rand() % (55 - 1 + 1) + 1;
                }while(Num5 == Num4 || Num5 == Num3 || Num5 == Num2 || Num5 == Num1);

                Num6 = rand() % (42 - 1 + 1) + 1;

                SortNumbers();
                //PrintToFile();        // Uncomment to print the results to QuickPicks.txt

                cout << setw(2) << Num1 << " "
                     << setw(2) << Num2 << " "
                     << setw(2) << Num3 << " "
                     << setw(2) << Num4 << " "
                     << setw(2) << Num5 << " "
                     << setw(2) << Num6 << endl << endl;
            }
        }
        else
            break;
    }
    return 0;
}

void SortNumbers()
{
    int Temp = 0;
    do
    {
        if(Num1 > Num2)
        {
            Temp = Num1;
            Num1 = Num2;
            Num2 = Temp;
        }
        if(Num2 > Num3)
        {
            Temp = Num2;
            Num2 = Num3;
            Num3 = Temp;
        }
        if(Num3 > Num4)
        {
            Temp = Num3;
            Num3 = Num4;
            Num4 = Temp;
        }
        if(Num4 > Num5)
        {
            Temp = Num4;
            Num4 = Num5;
            Num5 = Temp;
        }
    }while(Num1 > Num2 || Num2 > Num3 || Num3 > Num4 || Num4 > Num5);
}

void PrintToFile()
{
    ofstream appendFile("QuickPicks.txt", ios_base::app);

    if(appendFile.fail())
    {
        cerr << "Unable to write to file." << endl;
        exit(1);
    }

    appendFile << setw(2) << Num1 << " "
              << setw(2) << Num2 << " "
              << setw(2) << Num3 << " "
              << setw(2) << Num4 << " "
              << setw(2) << Num5 << " "
              << setw(2) << Num6 << endl;

    appendFile.close();
}
