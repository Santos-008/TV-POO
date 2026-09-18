CONTROLE DE TELEVISÃO - PYTHON

O projeto consiste na simulação de um controle remoto de TV usando Python, o programa mostra a tela da TV e o usuário pode controlá-la com os comandos do controle remoto.

COMANDOS DO CONTROLE:

'@' : Liga/Desliga
'>' : Avança o canal
'+' : Aumenta o volume
'-' : Diminui o volume
'0' : Sai do programa

Para esse projeto, usei a biblioteca rich para fazer toda a interface. Estruturei usando uma classe com um método para usar a TV, quando esse método é chamado, a TV é mostrada na tela e o código entra em looping para simular que a TV permaneça estática e o usuário possa interagir. O volume foi feito usando uma lista com caracteres em branco, onde a lista é transformada em texto e printada com as cores verde e branca adequadas com base no nível de volume atual para trazer o efeito de preenchimento de barra, uma lógica parecida foi usada para fazer os canais, uma lista de 1 a 5 onde toda vez que o usuário avança o canal, o próximo item da lista é pintado, simbolizando a navegação interativa.

Esse projeto tem como intuito o reforço do meu aprendizado em POO usando Python. Ao comparar minha solução com a do professor, percebi que o código dele ficou muito mais limpo e organizado, o que me fez perceber que tornei minha versão mais complexa e confusa do que era necessário. Ainda assim, acredito que essa versão menos enxuta, produzida sozinho, foi de extrema importância pro meu aprendizado. Reconheço que tenho muito a melhorar, mas entreguei uma versão com o funcionamento correto, agora é só aperfeiçoar!
