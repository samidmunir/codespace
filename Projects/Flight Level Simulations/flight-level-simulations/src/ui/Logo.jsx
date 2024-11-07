import styled from 'styled-components'

const StyledLogo = styled.div`
    text-align: center;
`

const StyledImg = styled.img`
    width: 275px;
    height: auto;
`

const Logo = () => {
    return (
        <StyledLogo>
            <StyledImg src='/public/Logo.png' alt='Logo' />
        </StyledLogo>
    )
}

export default Logo