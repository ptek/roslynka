from historia import HIST_DIR, HIST_FILE
import polars as pl
import hvplot.polars
from bokeh.resources import INLINE
from bokeh.models.formatters import DatetimeTickFormatter

HUMIDITY_PLOT_FILE=HIST_DIR+"wykres_wilgotnosci.html"
formatter = DatetimeTickFormatter(
    seconds = '%Ss',
    minsec = '%H:%M:%S',
    minutes = '%H:%M',
    hourmin = '%H:%M',
    hours = '%H:%M',
    days = '%Y-%m-%d',
    months = '%Y-%m',
    years = "%Y"
)

def wykres():
    df = pl.read_csv(HIST_FILE).with_columns([
        pl.col("czas").cast(pl.Datetime),
        pl.col("wilgotność").cast(pl.Int32)
    ]).sort("czas")
    print(df)
    plot_humidity = df.hvplot(x="czas", y="wilgotność", sort_date=False, xformatter=formatter, autorange="y", responsive=True)
    hvplot.save(plot_humidity, HUMIDITY_PLOT_FILE, resources=INLINE)

wykres()
