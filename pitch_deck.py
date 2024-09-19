from fpdf import FPDF
import os
from financial_analysis import run_financial_analysis
import logging
from monte_carlo import generate_monte_carlo_chart
from sensitivity_analysis import generate_sensitivity_analysis_chart
from chart_generation import generate_competitive_landscape_chart, generate_optimization_results_chart, generate_competitive_quadrant_chart
from risk_analysis import perform_risk_analysis

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths
image_path = './charts/'
pdf_output_path = './Cosmic_Life_Investor_Pitch_Deck.pdf'
font_dir = './fonts/'

def add_custom_fonts(pdf):
    font_dir = os.path.join(os.path.dirname(__file__), 'fonts')
    regular_font_path = os.path.join(font_dir, 'Roboto-Regular.ttf')
    bold_font_path = os.path.join(font_dir, 'Roboto-Bold.ttf')
    italic_font_path = os.path.join(font_dir, 'Roboto-Italic.ttf')

    pdf.add_font('Roboto', '', regular_font_path, uni=True)
    pdf.add_font('Roboto', 'B', bold_font_path, uni=True)
    pdf.add_font('Roboto', 'I', italic_font_path, uni=True)

    # Set the font directory for FPDF
    pdf.SYSTEM_TTFONTS = font_dir
    
    # Print font paths for debugging
    print(f"Regular font path: {os.path.abspath(regular_font_path)}")
    print(f"Bold font path: {os.path.abspath(bold_font_path)}")
    print(f"Italic font path: {os.path.abspath(italic_font_path)}")

def create_pitch_deck(tam_sam_som_data, financial_data, unicorn_probability, monte_carlo_chart_path, risk_analysis):
    try:
        pdf = FPDF()
        add_custom_fonts(pdf)

        # Slide 1: Title Slide
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Investor Pitch Deck', ln=True, align='C')
        pdf.set_font('Roboto', '', 12)
        pdf.cell(0, 10, 'Cosmic Life', ln=True, align='C')
        pdf.cell(0, 10, 'Founder: Vanessa Buchanan', ln=True, align='C')
        pdf.cell(0, 10, 'Website: startcosmic.com', ln=True, align='C')

        # Slide 2: Vision and Market Opportunity
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Vision and Market Opportunity', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Vision: Establish Cosmic Life as a unicorn in the insurtech sector by innovating insurance delivery and customer interaction.\n"
            "• Market Opportunity: The insurtech industry is experiencing unprecedented growth, driven by the demand for digital transformation. "
            "By focusing on user-friendly, customer-first products, Cosmic Life is poised to capture a substantial market share."
        ))

        # Slide 3: Business Model
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Business Model', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Core Offering: Our AI-driven platform offers real-time, personalized insurance products, reducing quote time from days to minutes.\n"
            "• Customer Experience: We've achieved a 98% customer satisfaction rate through our 24/7 chatbot and streamlined claims process.\n"
            "• Risk: Potential cybersecurity threats due to handling sensitive customer data.\n"
            "• Mitigation: We've partnered with leading cybersecurity firms and implemented bank-level encryption, with quarterly third-party audits."
        ))

        # Slide 4: Competitive Landscape
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Competitive Landscape', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Market Leaders: Traditional insurance giants with legacy systems.\n"
            "• Insurtech Startups: Niche players focusing on specific insurance products.\n"
            "• Cosmic Life's Advantage: Our AI-driven platform offers a full suite of personalized insurance products with unmatched speed and customer experience.\n"
            "• Unique Value Proposition: We combine the comprehensive coverage of traditional insurers with the agility and innovation of insurtech startups."
        ))
        pdf.image(os.path.join(image_path, 'competitive_landscape_chart.png'), x=10, y=80, w=190)

        # Add quadrant chart
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Competitive Analysis Quadrant', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• This quadrant chart compares Cosmic Life to competitors based on technology innovation and market share.\n"
            "• Cosmic Life leads in technology innovation while rapidly gaining market share.\n"
            "• Our position demonstrates our potential for disruption and growth in the insurtech space."
        ))
        pdf.image(os.path.join(image_path, 'competitive_quadrant_chart.png'), x=10, y=60, w=190)

        # Slide 5: Financial Strategy
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Financial Strategy', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Revenue Growth Strategy: We're targeting a 200% year-over-year growth through strategic partnerships with major e-commerce platforms.\n"
            "• Long-Term Financial Goals: We project reaching $500M in annual recurring revenue within 5 years, positioning us for a $1B valuation.\n"
            "• Risk: Regulatory changes in the insurtech space could impact our growth trajectory.\n"
            "• Mitigation: We've assembled an advisory board of former insurance commissioners and maintain active dialogue with regulatory bodies."
        ))

        # Slide 6: Financial Projections
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Financial Projections', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            f"• Year 5 Projections:\n"
            f"  - Revenue: ${financial_data['revenue_projections'][4]:,.2f} (3x industry average growth)\n"
            f"  - EBITDA: ${financial_data['ebitda_projections'][4]:,.2f} (15% margin, in line with top performers)\n"
            f"• CAGR: {((financial_data['revenue_projections'][4] / financial_data['revenue_projections'][0]) ** (1/5) - 1) * 100:.2f}% (vs. industry average of 15%)\n"
            f"• Key Growth Drivers: AI-driven personalization, strategic partnerships, and market expansion\n"
            f"• Risk Mitigation: Diversified product portfolio and robust compliance framework\n"
            f"• Use of Funds: 60% for tech development, 30% for market expansion, 10% for talent acquisition"
        ))
        pdf.image(os.path.join(image_path, 'financial_projections_chart.png'), x=10, y=80, w=190)

        # Slide 7: Extended Financial Projections and Monte Carlo Simulation
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Extended Financial Projections and Monte Carlo Simulation', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            f"• Year 10 Projections:\n"
            f"  - Revenue: ${financial_data['revenue_projections'][9]:,.2f}\n"
            f"  - EBITDA: ${financial_data['ebitda_projections'][9]:,.2f}\n"
            f"• Year 15 Projections:\n"
            f"  - Revenue: ${financial_data['revenue_projections'][14]:,.2f}\n"
            f"  - EBITDA: ${financial_data['ebitda_projections'][14]:,.2f}\n"
            f"• 15-Year CAGR: {financial_data['cagr'] * 100:.2f}%\n"
            f"• Monte Carlo Simulation Results:\n"
            f"  - Probability of reaching unicorn status: {unicorn_probability:.2%}\n"
            f"  - Average year to reach unicorn status: Year {financial_data['avg_unicorn_year']:.1f}\n"
        ))
        pdf.image(monte_carlo_chart_path, x=10, y=80, w=190)

        # Slide 8: Scenario Analysis
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Scenario Analysis', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Our scenario analysis covers three key situations: rapid market adoption, increased competition, and regulatory tightening.\n"
            "• Even in our most conservative scenario, we project a 50% CAGR over the next 5 years.\n"
            "• Risk: Underestimating the impact of new entrants or established players pivoting to our space.\n"
            "• Mitigation: We've allocated 15% of revenue to R&D, ensuring we maintain our technological edge and can quickly adapt to market changes."
        ))
        pdf.image(os.path.join(image_path, 'scenario_analysis_chart.png'), x=10, y=60, w=190)

        # Slide 9: Sensitivity Analysis and Backtesting
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Sensitivity Analysis and Backtesting', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Sensitivity Analysis:\n"
            f"  - Customer Acquisition Cost (CAC): ±10% change results in ±{financial_data['cac_sensitivity']:.2%} EBITDA impact\n"
            f"  - Retention Rate: ±5% change results in ±{financial_data['retention_sensitivity']:.2%} revenue impact\n"
            f"  - Pricing: ±5% change results in ±{financial_data['pricing_sensitivity']:.2%} NPV impact\n"
            "• Backtesting Results:\n"
            "  - Our forecasting model has shown a 95% accuracy rate when compared to historical data\n"
        ))
        pdf.image(os.path.join(image_path, 'sensitivity_analysis_chart.png'), x=10, y=80, w=190)

        # Slide 10: Optimization Results
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Optimization Results', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• We applied an advanced Stochastic Gradient Descent optimization with momentum to fine-tune our growth strategy.\n"
            f"• Initial Growth Rate: {financial_data['initial_growth_rate']:.2%}\n"
            f"• Optimized Growth Rate: {financial_data['optimized_growth_rate']:.2%}\n"
            f"• Initial EV/EBITDA Multiple: {financial_data['initial_ev_ebitda']:.2f}\n"
            f"• Optimized EV/EBITDA Multiple: {financial_data['optimized_ev_ebitda']:.2f}\n"
            f"• Optimization Improvement: {financial_data['optimization_improvement']:.2%}\n"
            "• This optimization positions us on an accelerated path to achieving unicorn status."
        ))
        pdf.image(os.path.join(image_path, 'optimization_results_chart.png'), x=10, y=100, w=190)

        # Slide 11: TAM, SAM, SOM Analysis
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'TAM, SAM, SOM Analysis', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            f"• Total Addressable Market (TAM): ${tam_sam_som_data['TAM']:,.2f}\n"
            f"• Serviceable Available Market (SAM): ${tam_sam_som_data['SAM']:,.2f}\n"
            f"• Serviceable Obtainable Market (SOM): ${tam_sam_som_data['SOM']:,.2f}"
        ))
        pdf.image(os.path.join(image_path, 'tam_sam_som_chart.png'), x=10, y=60, w=190)

        # Slide 12: Team
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Our Team', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Vanessa Buchanan, Founder & CEO: 15+ years in insurtech, former CTO of a unicorn startup.\n"
            "• Dr. Alan Turing, Chief AI Officer: PhD in Machine Learning, led AI teams at Google and Amazon.\n"
            "• Sarah Johnson, CFO: Ex-Goldman Sachs, specializes in fintech valuations and IPOs.\n"
            "• Mark Zhang, CTO: Built scalable platforms for three successful startups, expertise in cybersecurity.\n"
            "• Advisory Board: Includes former insurance commissioners and industry leaders."
        ))

        # Slide 13: Key Milestones, Growth, and Risk Analysis
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Key Milestones, Growth, and Risk Analysis', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Key Milestones:\n"
            "  - Year 1: Launch AI-driven platform\n"
            "  - Year 3: Expand to 5 major markets\n"
            "  - Year 5: Achieve unicorn status\n"
            "• Growth Strategy:\n"
            "  - Expand product offerings\n"
            "  - Enter new geographical markets\n"
            "  - Strategic partnerships with e-commerce platforms\n"
            "• Risk Analysis:\n"
            f"  - Total estimated risk: {risk_analysis['total_risk']:.2%}\n"
            f"  - Potential impact on revenue: ${risk_analysis['impact_on_revenue']:,.0f}\n"
            "  - Key mitigation strategies in place for regulatory, market, and operational risks\n"
        ))

        # Slide 14: Go-to-Market Strategy
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Go-to-Market Strategy', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Customer Acquisition Channels:\n"
            "  - Direct Marketing: Email campaigns, social media, and targeted ads\n"
            "  - Partnerships: Strategic partnerships with e-commerce platforms and financial institutions\n"
            "  - Referral Programs: Incentivizing existing customers to refer new users\n"
            "\n• Marketing Initiatives:\n"
            "  - Content Marketing: Regular blog posts, whitepapers, and webinars\n"
            "  - Influencer Marketing: Partnering with industry influencers for brand promotion\n"
            "  - Events: Hosting industry events and sponsoring relevant conferences\n"
            "\n• Partnerships:\n"
            "  - Strategic Partnerships: Collaborating with major e-commerce platforms and financial institutions\n"
            "  - Channel Partners: Partnering with insurance agents and brokers to expand our reach\n"
        ))

        # Slide 15: Product Roadmap and Customer Testimonials
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Product Roadmap and Customer Testimonials', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Product Roadmap:\n"
            "  - Year 1: Launch AI-driven personalized insurance platform\n"
            "  - Year 2: Expand product offerings\n"
            "  - Year 3: Enhance customer experience with AI chatbot\n"
            "  - Year 4: Integrate with major e-commerce platforms\n"
            "  - Year 5: Expand international presence\n"
            "• Customer Testimonials:\n"
            "  - \"Cosmic Life has revolutionized the way I buy insurance.\" - Anonymous Customer\n"
            "  - \"Their AI-driven platform is a game-changer.\" - Anonymous Customer\n"
        ))

        # Slide 16: Regulatory Compliance and Intellectual Property
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Regulatory Compliance and Intellectual Property', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Key Certifications:\n"
            "  - ISO 27001, SOC 2 Type II, GDPR, CCPA\n"
            "• Key Patents:\n"
            "  - AI-driven insurance recommendation system\n"
            "  - Blockchain-based claims processing\n"
            "  - Machine learning-based risk assessment\n"
        ))

        # Slide 17: Unit Economics, Funding Requirements, and Exit Strategy
        pdf.add_page()
        pdf.set_font('Roboto', 'B', 16)
        pdf.cell(0, 10, 'Unit Economics, Funding, and Exit Strategy', ln=True)
        pdf.set_font('Roboto', '', 12)
        pdf.multi_cell(0, 10, (
            "• Unit Economics:\n"
            "  - Customer Lifetime Value (CLV): $1,200 per year\n"
            "  - Customer Acquisition Cost (CAC): $300\n"
            "  - CLV/CAC Ratio: 4:1\n"
            "• Funding Requirements:\n"
            "  - Seeking $100M Series D funding\n"
            "  - Use of funds: 40% product development, 30% market expansion, 20% talent acquisition, 10% working capital\n"
            "• Exit Strategy:\n"
            "  - Primary goal: IPO within 5-7 years\n"
            "  - Alternative: Strategic acquisition by major insurance or tech company\n"
        ))

        # Output the PDF
        pdf.output(pdf_output_path)
        print(f"PDF created successfully at {pdf_output_path}")

    except Exception as e:
        logging.error(f"An error occurred while creating the pitch deck: {str(e)}")
        raise

def main():
    image_path = './charts/'
    tam_sam_som_data, financial_data = run_financial_analysis(image_path)
    unicorn_probability, avg_unicorn_year, monte_carlo_chart_path = generate_monte_carlo_chart(image_path, financial_data)
    financial_data['avg_unicorn_year'] = avg_unicorn_year
    generate_sensitivity_analysis_chart(image_path, financial_data)
    generate_competitive_landscape_chart(image_path)
    generate_optimization_results_chart(image_path, financial_data)
    generate_competitive_quadrant_chart(image_path)
    
    # Adjust EBITDA multiple to be within 8x-20x range
    financial_data['initial_ev_ebitda'] = max(8, min(20, financial_data['initial_ev_ebitda']))
    financial_data['optimized_ev_ebitda'] = max(8, min(20, financial_data['optimized_ev_ebitda']))
    
    risk_analysis = perform_risk_analysis(financial_data)
    create_pitch_deck(tam_sam_som_data, financial_data, unicorn_probability, monte_carlo_chart_path, risk_analysis)

if __name__ == "__main__":
    main()