# CUBO 3D

## Propriedades Matemáticas

- **Coordenadas 3D:** O cubo é definido por suas coordenadas 3D nos vértices. Cada vértice possui três coordenadas: x, y e z. Essas coordenadas determinam a forma e a posição do cubo no espaço tridimensional.

- **Rotação 3D:** A rotação do cubo é alcançada aplicando rotações nas coordenadas x, y e z dos vértices. Isso é feito usando matrizes de rotação, que envolvem funções trigonométricas como seno e cosseno. As rotações são especificadas pelos ângulos alpha, beta e gamma, que controlam a rotação em torno dos eixos x, y e z, respectivamente.

## Técnicas Programáticas

- **HTML e CSS:** O código HTML é usado para criar a estrutura da página, incluindo o elemento para o desenho do cubo e controles deslizantes. O CSS é usado para estilizar a página.

- **JavaScript:** O JavaScript é a linguagem de programação principal usada para implementar a lógica do projeto. Aqui estão as principais técnicas programáticas:

  - **Desenho em Canvas:** O é usado como o meio para desenhar o cubo. O contexto 2D (ctx) do `<canvas>` é usado para traçar as linhas.

  - **Rotação 3D:** A rotação 3D é implementada na função `rotatePoint`, que aplica matrizes de rotação para os vértices do cubo. Essas matrizes envolvem cálculos trigonométricos para calcular as novas coordenadas após a rotação.

  - **Atualização Interativa:** Os controles deslizantes permitem que o usuário defina os ângulos de rotação (alpha, beta e gamma) e, em seguida, a função `updateCubeRotation` é chamada para atualizar o desenho do cubo de acordo com as configurações do usuário.

  - **Event Listeners:** Event listeners são usados para detectar as mudanças nos controles deslizantes e responder a elas, chamando a função de atualização.

Essas propriedades matemáticas e técnicas programáticas combinadas permitem criar uma representação gráfica simples de um cubo 3D que pode ser girado interativamente usando controles deslizantes. É um projeto básico, mas demonstra os princípios fundamentais de desenho 3D e rotação em um ambiente web.

### No arquivo ***cubo3d_py3.py***, há uma versão em python 3 para o desenho 3D do cubo e rotação com controles deslizantes
