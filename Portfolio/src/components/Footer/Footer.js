import React from 'react';
import { AiFillGithub, AiFillTwitterCircle, AiFillLinkedin } from 'react-icons/ai';

import { SocialIcons } from '../Header/HeaderStyles';
import { CompanyContainer, FooterWrapper, LinkColumn, LinkItem, LinkList, LinkTitle, Slogan, SocialContainer, SocialIconsContainer } from './FooterStyles';

const Footer = () => {
  return (
    <FooterWrapper id="contact">
        <LinkList>
            <LinkColumn>
                <LinkTitle>Contact by Phone</LinkTitle>
                <LinkItem href="tel:208-352-2531">208-352-2531</LinkItem>
            </LinkColumn>
        </LinkList>
        <SocialIconsContainer>
            <CompanyContainer>
                <Slogan>Play Hard, Work Harder</Slogan>
            </CompanyContainer>
            <SocialContainer>

            <SocialIcons target="_blank" href="https://github.com/justinsgithub">
                <AiFillGithub size="3rem" />
            </SocialIcons>
        
            <SocialIcons target="_blank" href="https://www.linkedin.com/in/justinaawd/">
                <AiFillLinkedin size="3rem" />
            </SocialIcons>
        
            <SocialIcons target="_blank" href="https://twitter.com/LoveJustinTyler">
                <AiFillTwitterCircle size="3rem" />                
            </SocialIcons>

            </SocialContainer>
        </SocialIconsContainer>
    </FooterWrapper>
  );
};

export default Footer;
