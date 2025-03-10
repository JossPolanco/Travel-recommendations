-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-03-2025 a las 02:26:30
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `travel_recommendations`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `prd_get_places` (IN `chs_name` VARCHAR(100), IN `chs_distance` INT, `chs_budget` INT, IN `chs_weather` VARCHAR(200), IN `chs_season` VARCHAR(200))   BEGIN
    SELECT * FROM places 
    WHERE (chs_name IS NULL OR place LIKE CONCAT('%', chs_name, '%'))
    AND (chs_distance IS NULL OR distance <= chs_distance)
    AND (chs_budget IS NULL OR cost <= chs_budget)
    AND (chs_weather IS NULL OR weather LIKE CONCAT('%', chs_weather, '%'))
    AND (chs_season IS NULL OR seasons LIKE CONCAT('%', chs_season, '%'));
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `places`
--

CREATE TABLE `places` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) DEFAULT NULL,
  `distance` int(11) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `weather` varchar(200) DEFAULT NULL,
  `seasons` varchar(200) DEFAULT NULL,
  `information` varchar(500) DEFAULT NULL,
  `recommendation` varchar(500) DEFAULT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `img` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `places`
--

INSERT INTO `places` (`id`, `name`, `place`, `distance`, `cost`, `weather`, `seasons`, `information`, `recommendation`, `latitude`, `longitude`, `img`) VALUES
(6, 'Cancún', 'Playa,Resort,Ciudad turística', 2300, 15000, 'Cálido,Tropical,Húmedo,Soleado', 'Enero-Marzo,Abril-Junio,Octubre-Diciembre', 'Cancún es un destino turístico ubicado en la península de Yucatán, reconocido por sus hermosas playas de arena blanca y aguas cristalinas color turquesa. Ofrece una amplia variedad de hoteles, restaurantes, vida nocturna y actividades acuáticas. Es la puerta de entrada a la Riviera Maya y está cerca de importantes sitios arqueológicos mayas.', 'Lleva protector solar de alta protección, ropa ligera y sombrero. Evita la temporada de huracanes (julio-septiembre). Prueba los mariscos locales y visita cenotes cercanos. Ten cuidado con las corrientes marinas y respeta las banderas de advertencia en las playas.', 21.1619, -86.8515, '/static/img/places/puerto_vallarta.webp'),
(7, 'Guanajuato', 'Ciudad colonial,Patrimonio UNESCO,Ciudad histórica', 780, 8000, 'Templado,Seco,Fresco por las noches', 'Enero-Marzo,Abril-Junio,Octubre-Diciembre', 'Guanajuato es una ciudad colonial ubicada en el centro de México, reconocida por sus callejones empedrados, plazas pintorescas y arquitectura colorida. Fue un importante centro minero durante la época colonial y hoy es Patrimonio de la Humanidad. Es famosa por el Festival Internacional Cervantino, sus túneles subterráneos y el Callejón del Beso.', 'Lleva zapatos cómodos para caminar por sus empinadas calles empedradas. Visita durante el Festival Cervantino (octubre) para disfrutar de eventos culturales. Prueba las enchiladas mineras y los dulces típicos. La ciudad tiene un clima agradable casi todo el año, pero lleva un suéter para las noches frescas.', 21.019, -101.2574, ''),
(8, 'Oaxaca', 'Ciudad colonial,Destino cultural,Sitio gastronómico', 1400, 9000, 'Templado,Seco,Moderado', 'Enero-Marzo,Octubre-Diciembre', 'Oaxaca es una ciudad colonial en el sur de México conocida por su rica tradición culinaria, arquitectura histórica y vibrante cultura indígena. Es famosa por el mezcal, los moles, las artesanías y celebraciones como la Guelaguetza. Sus calles históricas albergan numerosos museos, galerías, mercados tradicionales y templos coloniales.', 'Prueba la diversa gastronomía local, especialmente los siete moles, tlayudas y chapulines. Visita los mercados tradicionales para comprar artesanías. La mejor época es durante la Guelaguetza (julio) o Día de Muertos (noviembre). Lleva ropa ligera pero con una chaqueta para las noches más frescas. Respeta las tradiciones indígenas locales.', 17.0732, -96.7266, ''),
(9, 'Barrancas del Cobre', 'Cañón,Área natural,Parque nacional', 220, 6000, 'Variable,Fresco en altura,Cálido en el fondo', 'Enero-Marzo,Octubre-Diciembre', 'Las Barrancas del Cobre son un sistema de cañones en la Sierra Tarahumara de Chihuahua, más grandes y profundos que el Gran Cañón de Colorado. Hogar de la comunidad indígena rarámuri, ofrece impresionantes vistas panorámicas, el tren Chepe que recorre paisajes espectaculares, y actividades como senderismo, ciclismo de montaña y tirolesas.', 'Viaja en el tren Chepe para disfrutar de las mejores vistas. Lleva ropa en capas ya que la temperatura varía significativamente entre el día y la noche y según la altitud. Respeta las costumbres de los rarámuris. Lleva calzado de senderismo resistente si planeas explorar los senderos. La mejor época es la temporada seca (octubre-abril).', 27.5502, -107.7887, ''),
(10, 'San Miguel de Allende', 'Ciudad colonial,Patrimonio UNESCO,Destino artístico', 850, 11000, 'Templado,Seco,Soleado', 'Enero-Marzo,Abril-Junio,Octubre-Diciembre', 'San Miguel de Allende es una ciudad colonial en el estado de Guanajuato, reconocida por su arquitectura barroca, calles empedradas y vibrante comunidad artística. Su icónica Parroquia de San Miguel Arcángel de estilo neogótico es el símbolo de la ciudad. Atrae a artistas, escritores y turistas de todo el mundo por su belleza, galerías de arte y escuelas de español.', 'Lleva zapatos cómodos para las calles empedradas. Prueba los restaurantes gourmet que combinan cocina mexicana e internacional. Disfruta del clima agradable durante el día, pero lleva un suéter para las noches frescas. Visita los baños termales cercanos. La ciudad es muy segura y caminable, ideal para explorar a pie.', 20.9144, -100.7452, ''),
(11, 'Puerto Vallarta', 'Playa,Bahía,Resort,Destino turístico', 950, 12000, 'Cálido,Tropical,Húmedo,Soleado', 'Enero-Marzo,Abril-Junio,Octubre-Diciembre', 'Puerto Vallarta es un destino turístico en la costa del Pacífico mexicano, famoso por sus playas, vida nocturna y el encanto de su centro histórico. La Bahía de Banderas ofrece oportunidades para avistamiento de ballenas, buceo y deportes acuáticos. Combina la belleza natural de la selva y montañas con la arquitectura tradicional mexicana.', 'Lleva protector solar y repelente de insectos. La mejor época para visitar es de noviembre a mayo (temporada seca). Prueba el pescado zarandeado y los mariscos frescos. Visita el Malecón al atardecer para disfrutar de esculturas y espectáculos callejeros. Si viajas entre diciembre y marzo, no te pierdas las excursiones de avistamiento de ballenas jorobadas.', 20.6534, -105.2253, 'static\\img\\places\\puerto_vallarta.webp'),
(12, 'Chichén Itzá', 'Zona arqueológica,Patrimonio UNESCO,Sitio histórico', 2200, 10000, 'Cálido,Húmedo,Tropical', 'Enero-Marzo,Octubre-Diciembre', 'Chichén Itzá es uno de los principales sitios arqueológicos mayas, ubicado en Yucatán. Nombrado Patrimonio de la Humanidad y una de las Nuevas Siete Maravillas del Mundo, destaca por la pirámide de Kukulcán (El Castillo), el Juego de Pelota, el Observatorio y el Cenote Sagrado. Fue un importante centro político y religioso de la civilización maya.', 'Visita temprano en la mañana para evitar multitudes y el calor intenso. Lleva sombrero, protector solar, agua y ropa ligera. Contrata un guía certificado para entender mejor la historia y simbolismo. Durante los equinoccios (marzo y septiembre) puedes presenciar el efecto de luz y sombra de la serpiente descendiendo por la pirámide. Combina tu visita con un refrescante baño en algún cenote cercano.', 20.6843, -88.5677, ''),
(13, 'Tulum', 'Zona arqueológica,Playa,Destino turístico', 2350, 13000, 'Cálido,Tropical,Húmedo,Soleado', 'Enero-Marzo,Abril-Junio,Octubre-Diciembre', 'Tulum combina ruinas mayas junto al mar Caribe con hermosas playas de arena blanca y aguas turquesa. Las ruinas arqueológicas están situadas sobre un acantilado frente al mar, creando un paisaje único. La zona se ha convertido en un destino eco-chic con hoteles boutique, restaurantes de moda y una atmósfera bohemia. Cerca hay cenotes y la Reserva de la Biosfera de Sian Ka\'an.', 'Visita las ruinas temprano para evitar multitudes y el calor. Combina cultura y naturaleza explorando los cenotes cercanos. La zona es perfecta para ciclismo, lleva ropa ligera pero también protección contra el sol. Prueba la cocina local fusionada con tendencias internacionales en los restaurantes ecológicos. Es recomendable rentar un auto para explorar los alrededores.', 20.2114, -87.4295, 'static\\img\\places\\tulum.webp'),
(14, 'Ciudad de México', 'Ciudad capital,Metrópoli,Centro cultural', 1200, 10000, 'Templado,Variable,Fresco por las noches', 'Enero-Marzo,Octubre-Diciembre', 'Ciudad de México es la capital y una de las ciudades más grandes del mundo. Combina historia prehispánica, colonial y moderna con una vibrante escena cultural y gastronómica. Entre sus atractivos destacan el Zócalo, Palacio de Bellas Artes, Museo Nacional de Antropología, Templo Mayor, Chapultepec, Xochimilco y Teotihuacán en sus cercanías.', 'Usa el metro para moverte eficientemente. Visita durante la temporada seca (noviembre-abril). La ciudad está a gran altitud, toma tiempo para aclimatarte. Prueba los tacos callejeros, pero elige puestos concurridos y con buena higiene. Visita los museos los días entre semana para evitar multitudes. Planifica bien tus rutas debido al tráfico intenso.', 19.4326, -99.1332, ''),
(15, 'Real de Catorce', 'Pueblo mágico,Pueblo minero,Sitio histórico', 720, 7000, 'Semiárido,Fresco,Seco', 'Enero-Marzo,Abril-Junio,Octubre-Diciembre', 'Real de Catorce es un antiguo pueblo minero en San Luis Potosí, considerado Pueblo Mágico. Se accede a través de un túnel de 2.3 km y conserva un ambiente místico con calles empedradas y edificios coloniales. Es un sitio sagrado para los huicholes y famoso por el desierto de Wirikuta. El pueblo fantasma atrae a turistas en busca de experiencias espirituales y aventuras en el desierto.', 'Lleva ropa abrigadora para las noches frías de montaña. Contrata un tour en Jeep para explorar el desierto y las minas abandonadas. Respeta los rituales y territorios sagrados de los huicholes. El acceso es a través de un túnel angosto, considera esto si sufres de claustrofobia. Prueba el mezcal local y la comida tradicional del desierto.', 23.6882, -100.8926, '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `places`
--
ALTER TABLE `places`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `places`
--
ALTER TABLE `places`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
