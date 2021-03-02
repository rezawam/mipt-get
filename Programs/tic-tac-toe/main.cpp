#include <ncurses.h>

int main()
{
	char ch = 'X';
	initscr();
	while (1)
	{
		mvprintw(0, 0, " %c  | %c  |  %c \n", ch, ch, ch);
		printw("--------------\n");
		mvprintw(2, 0, " %c  | %c  |  %c \n", ch, ch, ch);
		printw("--------------\n");
		mvprintw(4, 0, " %c  | %c  |  %c \n", ch, ch, ch);
		mvprintw(6, 0, "Press any key: ");
		ch = getch();
		refresh();
	}
		endwin();
	return 0;
}
