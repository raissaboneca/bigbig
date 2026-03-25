
const TOTAL_VEHICLES = 5000;
let vehicles = [];
let map, markersLayer;
let isFailureSimulated = false;

// 1. Inicialização do Mapa
function initMap() {
    map = L.map('map').setView([-15.7801, -47.9292], 4); // Centro do Brasil
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png').addTo(map);
    markersLayer = L.layerGroup().addTo(map);
}

// 2. Geração de Dados (Big Data Setup)
function createInitialFrota() {
    for (let i = 0; i < TOTAL_VEHICLES; i++) {
        vehicles.push({
            id: i,
            lat: -10 - Math.random() * 20, // Randômico pelo Brasil
            lon: -40 - Math.random() * 20,
            speed: Math.floor(Math.random() * 90),
            status: 'online',
            history: [] // Retenção histórica
        });
    }
}

// 3. Motor de Simulação e Otimização
function updateSimulation() {
    let errorCount = 0;
    markersLayer.clearLayers();

    // Simulando processamento em lote (Batch Processing)
    vehicles.forEach(v => {
        // Plano de Contingência: Falha de Sinal
        if (isFailureSimulated && Math.random() > 0.8) {
            v.status = 'offline';
            errorCount++;
        } else {
            v.status = 'online';
            // Otimização de Rota Básica: Move levemente em direção a um destino fixo (ex: Porto de Santos)
            const target = { lat: -23.96, lon: -46.33 };
            v.lat += (target.lat - v.lat) * 0.0001 * Math.random();
            v.lon += (target.lon - v.lon) * 0.0001 * Math.random();
            
            // Retenção Histórica (últimas 5 posições)
            v.history.push([v.lat, v.lon]);
            if (v.history.length > 5) v.history.shift();
        }

        // Renderização Otimizada: Apenas pontos (Canvas seria melhor para >10k, mas pontos resolvem 5k)
        if (v.id % 5 === 0) { // Renderiza 1 a cada 5 para performance no navegador
            const color = v.status === 'online' ? '#3b82f6' : '#ef4444';
            L.circleMarker([v.lat, v.lon], {
                radius: 2,
                color: color,
                fillOpacity: 0.8
            }).addTo(markersLayer);
        }
    });

    document.getElementById('total-trucks').innerText = TOTAL_VEHICLES.toLocaleString();
    document.getElementById('total-errors').innerText = errorCount;
}

function simulateFailure() {
    isFailureSimulated = !isFailureSimulated;
    document.getElementById('alert-box').style.display = isFailureSimulated ? 'block' : 'none';
}

// Iniciar
initMap();
createInitialFrota();
setInterval(updateSimulation, 1000); // Atualização "Real-Time"
