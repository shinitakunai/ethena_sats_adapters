from constants.integration_ids import IntegrationID
from utils.penpie import PENPIEIntegration
from constants.penpie import rsUSDe_26SEP2024, rsUSDe_26SEP2024_DEPLOYMENT_BLOCK   
from constants.chains import Chain
from constants.penpie import PENDLE_LOCKER_ETHEREUM

if __name__ == "__main__":
    penpie_integration = PENPIEIntegration(
        IntegrationID.PENPIE_rsUSDe_26SEP2024_LPT,
        rsUSDe_26SEP2024_DEPLOYMENT_BLOCK,
        rsUSDe_26SEP2024,
        Chain.ETHEREUM,
        20,
        1,
        [PENDLE_LOCKER_ETHEREUM]

    )
    print(penpie_integration.get_participants())
    # print(penpie_integration.get_balance("0x404581FA706E4E0d649A40eA503f9bCee3D2d76c", "latest"))