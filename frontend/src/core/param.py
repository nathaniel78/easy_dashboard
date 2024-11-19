from dotenv import load_dotenv
import os

load_dotenv()

#-------- Definindo parametros de configuração --------#
IMAGE_LOGO = os.getenv(
        "IMAGE_LOGO_URL", 
        default="https://images2.imgbox.com/65/6f/AxFowANl_o.jpg"
        )
SESSION_TIME = os.getenv(
        "SESSION_TIME", 
        default=300
        )
FOOTER_COPYRIGTH = '© 2024 EasyDashboard. Uso restrito a fins comerciais mediante licenciamento. <a href="https://github.com/nathaniel78/easy_dashboard" target="_blank">Git do projeto<a/>'
CHART_WIDTH = 900
CHART_HEIGHT = 400