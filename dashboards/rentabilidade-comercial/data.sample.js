/* Amostra sintética para a publicação pública. A base real fica fora do GitHub. */
window.DASHBOARD_SAMPLE_DATA = {
  meta: { periodoInicial: '2025-01', periodoFinal: '2025-06', businesses: ['Varejo Pet', 'Varejo Casa'] },
  monthly: [
    { periodo: '2025-01', business: 'Varejo Pet', faturamento: 420000, margem: 61000, tonelagem: 120, linhas: 480 },
    { periodo: '2025-02', business: 'Varejo Pet', faturamento: 445000, margem: 67000, tonelagem: 127, linhas: 505 },
    { periodo: '2025-03', business: 'Varejo Pet', faturamento: 468000, margem: 72000, tonelagem: 132, linhas: 530 },
    { periodo: '2025-04', business: 'Varejo Casa', faturamento: 390000, margem: 54000, tonelagem: 114, linhas: 440 },
    { periodo: '2025-05', business: 'Varejo Casa', faturamento: 425000, margem: 62000, tonelagem: 121, linhas: 470 },
    { periodo: '2025-06', business: 'Varejo Casa', faturamento: 452000, margem: 69000, tonelagem: 129, linhas: 498 }
  ],
  products: [
    { periodo: '2025-01', business: 'Varejo Pet', produto: 'Ração premium', faturamento: 175000, margem: 31000 },
    { periodo: '2025-02', business: 'Varejo Pet', produto: 'Higiene e cuidados', faturamento: 128000, margem: 22000 },
    { periodo: '2025-03', business: 'Varejo Pet', produto: 'Acessórios', faturamento: 108000, margem: 19000 },
    { periodo: '2025-04', business: 'Varejo Casa', produto: 'Organização', faturamento: 145000, margem: 21000 },
    { periodo: '2025-05', business: 'Varejo Casa', produto: 'Cozinha', faturamento: 132000, margem: 20000 },
    { periodo: '2025-06', business: 'Varejo Casa', produto: 'Limpeza', faturamento: 119000, margem: 18000 }
  ],
  customers: [
    { business: 'Varejo Pet', cliente: 'Cliente exemplo A', faturamento: 620000, margem: 98000, margem_pct: 0.158, tonelagem: 190, linhas: 42, produtos_distintos: 18, meses_ativos: 6, meses_sem_compra: 0, churn: 'Ativo', grupo_rfv: 'Campeões', cluster: 1, grupo_cliente: 'Estratégico', variacao_2025: 0.14 },
    { business: 'Varejo Pet', cliente: 'Cliente exemplo B', faturamento: 310000, margem: 39000, margem_pct: 0.126, tonelagem: 112, linhas: 24, produtos_distintos: 10, meses_ativos: 5, meses_sem_compra: 1, churn: 'Em risco', grupo_rfv: 'Fiéis', cluster: 1, grupo_cliente: 'Recorrente', variacao_2025: -0.04 },
    { business: 'Varejo Pet', cliente: 'Cliente exemplo C', faturamento: 80000, margem: 9000, margem_pct: 0.113, tonelagem: 31, linhas: 8, produtos_distintos: 4, meses_ativos: 2, meses_sem_compra: 3, churn: 'Churn observado', grupo_rfv: 'Em risco de perda', cluster: 2, grupo_cliente: 'Ocasional', variacao_2025: -0.31 },
    { business: 'Varejo Casa', cliente: 'Cliente exemplo D', faturamento: 510000, margem: 72000, margem_pct: 0.141, tonelagem: 156, linhas: 35, produtos_distintos: 15, meses_ativos: 6, meses_sem_compra: 0, churn: 'Ativo', grupo_rfv: 'Campeões', cluster: 1, grupo_cliente: 'Estratégico', variacao_2025: 0.09 },
    { business: 'Varejo Casa', cliente: 'Cliente exemplo E', faturamento: 175000, margem: 23000, margem_pct: 0.131, tonelagem: 64, linhas: 15, produtos_distintos: 7, meses_ativos: 4, meses_sem_compra: 2, churn: 'Em risco', grupo_rfv: 'Potencial', cluster: 2, grupo_cliente: 'Recorrente', variacao_2025: 0.06 },
    { business: 'Varejo Casa', cliente: 'Cliente exemplo F', faturamento: 54000, margem: 5000, margem_pct: 0.093, tonelagem: 19, linhas: 5, produtos_distintos: 3, meses_ativos: 1, meses_sem_compra: 5, churn: 'Churn observado', grupo_rfv: 'Ocasional', cluster: 2, grupo_cliente: 'Ocasional', variacao_2025: -0.45 }
  ]
};
