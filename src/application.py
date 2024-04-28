##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: application.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la aplicación que sirve la UI y la lógica 
#   del componente
#
#-------------------------------------------------------------------------
from src.view.dashboard import Dashboard
import dash_bootstrap_components as dbc
import dash
from dash import Input, Output, callback

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.title = "ETL"

dashboard = Dashboard()

app.layout = dashboard.document()

@app.callback(
    Output('numero-productos', 'children'),
    [Input('date-prod-vendidos-input-1', 'date'),
    Input('date-prod-vendidos-input-2', 'date')]
)
def obtener_numero_productos_vendidos_por_fecha_wrapper(fecha_inicio, fecha_fin):
    return dashboard.obtener_numero_productos_vendidos_por_fecha(fecha_inicio, fecha_fin)