# Tic Tac Toe Oyunu ve Yapay Zeka Ajanı

Bu proje, Python ve Pygame kütüphanesi kullanılarak geliştirilmiş bir Tic Tac Toe oyununu içerir. Ayrıca, oyunu öğrenmek ve insan oyuncuya karşı oynamak için bir yapay zeka ajanı da bulunmaktadır.

![12](https://github.com/ZekiAkkan/TicTacToe_Qlearning/assets/88339263/c554b8a1-ab96-4603-a56c-0b6f311525c1)
![13](https://github.com/ZekiAkkan/TicTacToe_Qlearning/assets/88339263/82a5109a-8eb6-432e-8db4-8e80e72b6876)
![14](https://github.com/ZekiAkkan/TicTacToe_Qlearning/assets/88339263/f2e6ced0-82ef-4349-bf1b-e222ee381694)


## Nasıl Çalıştırılır?

1. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirin ve yükleyin.
2. Projeyi klonlayın veya indirin.
3. Gerekli bağımlılıkları yüklemek için terminalde veya komut isteminde şu komutu çalıştırın:
```bash
pip install -r requirements.txt 
```
4. Oyunu başlatmak için `main.py` dosyasını çalıştırın.

## Oyun Nasıl Oynanır?

Oyun, insan oyuncuya karşı oynamak için bir arayüz sağlar. Oyun tahtası 3x3'lük bir ızgaradan oluşur ve oyuncuların sırayla hamle yapması beklenir.

## Yapay Zeka Ajanı

Ajanın öğrenme sürecini gözlemlemek istiyorsanız, `Agent` sınıfının `train_brain_x_byrandom` yöntemini kullanarak eğitim turu sayısını belirleyebilirsiniz. Bu yöntem, ajanı rastgele hamleler yaparak öğrenir.

## Sonuçlar

Oyunun sonucunu görmek için sonucu ekranda görüntülemek üzere sonuçlar dosyasını kullanabilirsiniz.

## Proje Yapısı

- `main.py`: Oyunun başlatılması ve çalıştırılması için ana dosya.
- `TicTacToe.py`: Tic Tac Toe oyununu yöneten `TicTacToe` sınıfını içerir.
- `Agent.py`: Yapay zeka ajanını temsil eden `Agent` sınıfını içerir.


## Katkılar

Proje sahibi: Zeki Akkan

Projeye katkıda bulunmak isterseniz lütfen bir çekme isteği gönderin veya bir sorun açın. Geri bildirimleriniz ve katkılarınız memnuniyetle karşılanacaktır!

# Tic Tac Toe Game and AI Agent

This project contains a Tic Tac Toe game developed using Python and the Pygame library. Additionally, it includes an artificial intelligence agent to learn the game and play against a human player.

## How to Run?

1. If Python is not installed, download and install Python from the [official Python website](https://www.python.org/downloads/).
2. Clone or download the project.
3. Install the required dependencies by running the following command in the terminal or command prompt:
```bash
pip install -r requirements.txt 
```
4. To start the game, run the `main.py` file.

## How to Play the Game?

The game provides an interface for playing against a human player. The game board consists of a 3x3 grid, and players take turns making moves.

## AI Agent

If you want to observe the learning process of the agent, you can specify the number of training rounds using the `train_brain_x_byrandom` method of the `Agent` class. This method allows the agent to learn by making random moves.

## Results

You can use the results file to view the outcome of the game.

## Project Structure

- `main.py`: The main file for starting and running the game.
- `TicTacToe.py`: Contains the `TicTacToe` class that manages the Tic Tac Toe game.
- `Agent.py`: Contains the `Agent` class representing the artificial intelligence agent.

## Contributions

Project owner: Zeki Akkan

If you would like to contribute to the project, please submit a pull request or open an issue. Your feedback and contributions are welcome!
