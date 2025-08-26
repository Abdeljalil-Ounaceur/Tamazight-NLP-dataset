#!/usr/bin/env python3
"""
PDF Preview Script for Tamazight-English Dictionary
This script provides a quick preview of the PDF structure without loading the entire content.
"""

import PyPDF2
import pandas as pd
import tabula
import os

def preview_pdf_info(pdf_path):
    """Get basic PDF information without reading all content"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"PDF Information:")
            print(f"- Total pages: {num_pages}")
            print(f"- File size: {os.path.getsize(pdf_path) / (1024*1024):.2f} MB")
            
            # Read first few pages to understand structure
            print(f"\n--- Sample from first page ---")
            first_page = pdf_reader.pages[0]
            sample_text = first_page.extract_text()[:500]
            print(sample_text)
            
            print(f"\n--- Sample from middle page ---")
            if num_pages > 10:
                middle_page = pdf_reader.pages[num_pages//2]
                middle_text = middle_page.extract_text()[:500]
                print(middle_text)
            
            return num_pages
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return 0

def detect_tables_preview(pdf_path, max_pages_to_check=5):
    """Detect tables in first few pages to understand structure"""
    try:
        print(f"\n--- Detecting tables in first {max_pages_to_check} pages ---")
        
        # Try to detect tables using tabula
        tables = tabula.read_pdf(pdf_path, pages=f"1-{max_pages_to_check}", multiple_tables=True)
        
        print(f"Found {len(tables)} potential tables in first {max_pages_to_check} pages")
        
        for i, table in enumerate(tables[:3]):  # Show first 3 tables
            print(f"\nTable {i+1} shape: {table.shape}")
            print(f"Columns: {list(table.columns)}")
            print("Sample data:")
            print(table.head(3))
            print("-" * 50)
            
        return len(tables)
    except Exception as e:
        print(f"Error detecting tables: {e}")
        return 0

if __name__ == "__main__":
    pdf_path = "Tamazight-English-Dictionary-2007.pdf"
    
    if os.path.exists(pdf_path):
        num_pages = preview_pdf_info(pdf_path)
        if num_pages > 0:
            detect_tables_preview(pdf_path)
    else:
        print(f"PDF file not found: {pdf_path}")
