import hidden_turtle
import matplotlib.pyplot as plt
import random


def random_walk(n):
    hidden_turtle.setposition(0,0)

    for i in range(n):
        hidden_turtle.setheading(random.random()*360)

        # For doing a 1D walk:
        # hidden_turtle.setheading(random.choice([180,0]))
        hidden_turtle.forward(10)

    return hidden_turtle.position()


n = 300
end_pos_list = []
for i in range(1000):
    end_pos = random_walk(n)
    end_pos_list.append(end_pos)


# This is for the 1D section:

# s_n_list = []
# for i in end_pos_list:
#     s_n_list.append(i[0])
# 
# mean_s = sum(s_n_list) / len(s_n_list)
# 
# plt.hist(s_n_list, 10)
# plt.axvline(mean_s, color = "r", lw =3)
# plt.show()


s_n_squared_list = []
for i in end_pos_list:
    s_n_squared_list.append(i[0]**2 + i[1]**2)

mean_sq = sum(s_n_squared_list) / len(s_n_squared_list)


plt.hist(s_n_squared_list, 20)
plt.axvline(mean_sq, color = "r", lw = 6)
plt.axvline(10**2 * n, color = "g", lw = 3)
plt.show()

s_n_list = []
for i in end_pos_list:
    s_n_list.append(i)


hidden_turtle.hist2d(end_pos_list, 20)
plt.show()
